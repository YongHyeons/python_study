import html
import requests
import xml.etree.ElementTree as ET
from urllib.parse import quote
from flask import Flask, request

from rss_reader import get_rss_data, get_article

app = Flask(__name__)

PAGE_STYLE = '''
    body {
        margin: 0;
        padding: 0;
        font-family: Arial, "맑은 고딕", sans-serif;
        background-color: #f4f6f8;
        color: #222;
    }

    header {
        background-color: #1f2937;
        color: white;
        padding: 30px;
        text-align: center;
    }

    header h1 {
        margin: 0;
        font-size: 32px;
    }

    header p {
        margin-top: 10px;
        color: #d1d5db;
    }

    main {
        max-width: 1000px;
        margin: 30px auto;
        padding: 0 20px;
    }

    .summary {
        background-color: white;
        padding: 20px;
        margin-bottom: 20px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }

    .news-card {
        display: flex;
        gap: 20px;
        background-color: white;
        padding: 20px;
        margin-bottom: 15px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }

    .news-index {
        min-width: 40px;
        height: 40px;
        border-radius: 50%;
        background-color: #2563eb;
        color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        font-weight: bold;
    }

    .news-content h2 {
        margin: 0;
        font-size: 20px;
    }

    .news-content a {
        color: #111827;
        text-decoration: none;
    }

    .news-content a:hover {
        color: #2563eb;
        text-decoration: underline;
    }

    .date {
        color: #6b7280;
        font-size: 14px;
        margin: 8px 0;
    }

    .description {
        line-height: 1.6;
        color: #374151;
    }

    .back-link {
        display: inline-block;
        margin-bottom: 20px;
        color: #2563eb;
        text-decoration: none;
        font-weight: bold;
    }

    .article {
        background-color: white;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }

    .article h1 {
        margin-top: 0;
        font-size: 26px;
        line-height: 1.4;
    }

    .article-body p {
        line-height: 1.9;
        color: #374151;
        margin: 0 0 16px;
    }

    .article-body img {
        display: block;
        max-width: 100%;
        height: auto;
        margin: 16px auto;
        border-radius: 8px;
    }

    .source-link {
        display: inline-block;
        margin-top: 20px;
        color: #6b7280;
        font-size: 14px;
    }
'''


def render_news_item(index, news):
    title = html.escape(news['title'])
    # 매경 링크가 아니라 내 사이트의 상세 페이지로 연결한다.
    detail_url = '/article?url=' + quote(news['url'], safe='')
    published_at = html.escape(news['published_at'])
    description = html.escape(news['description'])

    return f'''
        <article class="news-card">
            <div class="news-index">{index}</div>
            <div class="news-content">
                <h2>
                    <a href="{detail_url}">
                        {title}
                    </a>
                </h2>
                <p class="date">{published_at}</p>
                <p class="description">{description}</p>
            </div>
        </article>
    '''


def render_page(data):
    channel_title = html.escape(data['channel_title'])
    last_build_date = html.escape(data['last_build_date'])
    news_list = data['news_list']

    if news_list:
        news_html = ''.join(
            render_news_item(index, news)
            for index, news in enumerate(news_list, start=1)
        )
    else:
        news_html = '<p>가져온 뉴스가 없습니다.</p>'

    return f'''
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>{channel_title} 뉴스 목록</title>
        <style>{PAGE_STYLE}</style>
    </head>
    <body>
        <header>
            <h1>{channel_title}</h1>
            <p>Flask RSS 뉴스 페이지</p>
        </header>

        <main>
            <section class="summary">
                <h2>수집 정보</h2>
                <p>총 기사 수: {len(news_list)}개</p>
                <p>마지막 갱신일: {last_build_date}</p>
            </section>
            {news_html}
        </main>
    </body>
    </html>
    '''


def render_article_page(article):
    title = html.escape(article['title'])
    source_url = html.escape(article['source_url'])

    parts = []
    for block in article['blocks']:
        if block['type'] == 'image':
            src = html.escape(block['value'])
            parts.append(f'<img src="{src}" alt="" loading="lazy">')
        else:
            parts.append(f'<p>{html.escape(block["value"])}</p>')

    body_html = ''.join(parts) if parts else '<p>본문을 가져오지 못했습니다.</p>'

    return f'''
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
        <style>{PAGE_STYLE}</style>
    </head>
    <body>
        <header>
            <h1>매일경제 뉴스</h1>
            <p>Flask RSS 뉴스 페이지</p>
        </header>

        <main>
            <a class="back-link" href="/">← 목록으로</a>
            <article class="article">
                <h1>{title}</h1>
                <div class="article-body">
                    {body_html}
                </div>
                <a class="source-link" href="{source_url}" target="_blank">매경 원문 보기</a>
            </article>
        </main>
    </body>
    </html>
    '''


@app.route('/')
def index():
    try:
        data = get_rss_data()
    except requests.exceptions.Timeout:
        return '<h1>RSS 요청 시간이 초과되었습니다.</h1><p>잠시 후 다시 시도하세요.</p>'
    except requests.exceptions.RequestException as error:
        return f'<h1>RSS 요청 실패</h1><p>{html.escape(str(error))}</p>'
    except ET.ParseError as error:
        return f'<h1>XML 파싱 실패</h1><p>{html.escape(str(error))}</p>'

    return render_page(data)


@app.route('/article')
def article():
    url = request.args.get('url', '')

    if not url:
        return '<h1>잘못된 접근입니다.</h1><p><a href="/">목록으로</a></p>', 400

    try:
        data = get_article(url)
    except ValueError as error:
        return f'<h1>{html.escape(str(error))}</h1><p><a href="/">목록으로</a></p>', 400
    except requests.exceptions.Timeout:
        return '<h1>기사 요청 시간이 초과되었습니다.</h1><p><a href="/">목록으로</a></p>'
    except requests.exceptions.RequestException as error:
        return f'<h1>기사 요청 실패</h1><p>{html.escape(str(error))}</p><p><a href="/">목록으로</a></p>'

    return render_article_page(data)
