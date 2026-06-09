import threading
import webbrowser

from app import app


def open_browser():
    webbrowser.open('http://127.0.0.1:5000')


def main():
    print('뉴스 웹 서버를 시작합니다.')
    print('브라우저 주소: http://127.0.0.1:5000')
    print('서버를 종료하려면 콘솔에서 Ctrl + C 를 누르세요.')

    timer = threading.Timer(1.0, open_browser)
    timer.start()

    app.run(
        host='127.0.0.1',
        port=5000,
        debug=False,
        threaded=True
    )


if __name__ == '__main__':
    main()