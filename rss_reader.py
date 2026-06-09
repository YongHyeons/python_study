import requests
import xml.etree.ElementTree as ET
from urllib.parse import urlparse
from bs4 import BeautifulSoup

RSS_URL = 'https://www.mk.co.kr/rss/50000001/'

# 본문 스크랩을 허용할 도메인 (다른 사이트 요청 차단 — 보안)
ALLOWED_HOST = 'www.mk.co.kr'

# mk.co.kr 등 일부 사이트는 기본 python-requests UA를 차단한다.
HEADERS = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/124.0 Safari/537.36'
    )
}

# (연결 타임아웃, 읽기 타임아웃) — 서버가 응답을 붙잡고 있어도 무한 대기하지 않는다.
TIMEOUT = (5, 10)


def get_text(parent, tag_name):
    tag = parent.find(tag_name)

    if tag is None:
        return ''

    if tag.text is None:
        return ''

    return tag.text.strip()


def get_article(url):
    """기사 URL에 들어가 본문을 스크랩한다. {title, paragraphs, source_url} 반환."""
    if urlparse(url).hostname != ALLOWED_HOST:
        raise ValueError('허용되지 않은 주소입니다.')

    print(f'[rss] 본문 요청: {url}', flush=True)
    response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    title_tag = soup.select_one('h2.news_ttl') or soup.find('title')
    title = title_tag.get_text(strip=True) if title_tag else ''

    body_tag = soup.select_one('#article_body')

    # 본문을 문단(text)과 이미지(image)가 등장 순서대로 섞인 블록 리스트로 만든다.
    blocks = []

    if body_tag is not None:
        for tag in body_tag.find_all(['p', 'img']):
            if tag.name == 'img':
                src = tag.get('src') or tag.get('data-src') or ''
                if src.startswith('http'):
                    blocks.append({'type': 'image', 'value': src})
            else:
                text = tag.get_text(strip=True)
                if text:
                    blocks.append({'type': 'text', 'value': text})

    print(f'[rss] 본문 수신: 블록 {len(blocks)}개', flush=True)

    return {
        'title': title,
        'blocks': blocks,
        'source_url': url,
    }


def get_rss_data(rss_url=RSS_URL):
    print(f'[rss] 요청 시작: {rss_url}', flush=True)
    response = requests.get(rss_url, headers=HEADERS, timeout=TIMEOUT)
    print(f'[rss] 응답 수신: status={response.status_code}', flush=True)
    response.raise_for_status()

    root = ET.fromstring(response.text)

    channel = root.find('channel')

    if channel is None:
        return {
            'channel_title': '',
            'channel_link': '',
            'last_build_date': '',
            'news_list': [],
        }

    channel_title = get_text(channel, 'title')
    channel_link = get_text(channel, 'link')
    last_build_date = get_text(channel, 'lastBuildDate')

    items = channel.findall('item')

    news_list = []

    for item in items:
        news = {
            'title': get_text(item, 'title'),
            'url': get_text(item, 'link'),
            'published_at': get_text(item, 'pubDate'),
            'description': get_text(item, 'description'),
            'source': channel_title,
        }

        news_list.append(news)

    return {
        'channel_title': channel_title,
        'channel_link': channel_link,
        'last_build_date': last_build_date,
        'news_list': news_list,
    }


if __name__ == '__main__':
    data = get_rss_data()

    print('채널 제목:', data['channel_title'])
    print('채널 링크:', data['channel_link'])
    print('마지막 갱신일:', data['last_build_date'])
    print('기사 개수:', len(data['news_list']))
    print('=' * 50)

    for index, news in enumerate(data['news_list'], start=1):
        print(f'[{index}] {news["title"]}')
        print(f'링크: {news["url"]}')
        print(f'발행일: {news["published_at"]}')
        print('-' * 50)