from . import websocket, todos, router
import json
import datetime

try:
    from firebase_admin import messaging
except ImportError:
    pass

def __setup__ (app, mntopt):
    app.mount ('/todos', todos)
    app.mount ('/router', router)
    app.mount ('/websocket', websocket)


def __mount__ (app, mntopt):
    @app.route ("", methods = ["GET"])
    def index (was):
        return was.render ('examples/index.j2', layout = 'quanta')

    @app.route ("/tutorial", methods = ["GET"])
    def tutorial (was):
        return was.render_or_API (
            'examples/tutorial.j2',
            record_count = 66,
            item_list = [{'idx': 944, 'category': '정치', 'subject': '외교부 "지소미아 종료는 잠정조치"..日수출규제 철', 'uid': 'UNITTEST-CONTENT', 'news_url': 'https://www.yna.co.kr/view/AKR20200219076900004', 'status': 1, 'site_thumbnail_uid': 'VPnYIkkbTVVNMpKNZia0J1', 'nick_name': '세미콘 네트웍스', 'comment_count': 66, 'sympathy': 429, 'not_sympathy': 592, 'report_count': None}, {'idx': 943, 'category': '정치', 'subject': '여의도 증권사 건물 식당서 칼부림..2명 중상(종합)', 'uid': 'UNITTEST-CONTENT', 'news_url': 'https://www.yna.co.kr/view/AKR20200219076900004', 'status': 1, 'site_thumbnail_uid': 'VPnYIkkbTVVNMpKNZia0J1', 'nick_name': '세미콘 네트웍스', 'comment_count': 83, 'sympathy': 195, 'not_sympathy': 9, 'report_count': None}, {'idx': 942, 'category': '정책', 'subject': '조명래 장관 "中 공장 멈춰 하늘 맑아졌다? 근거 없다"', 'uid': 'UNITTEST-CONTENT', 'news_url': 'https://www.yna.co.kr/view/AKR20200219076900004', 'status': 1, 'site_thumbnail_uid': 'VPnYIkkbTVVNMpKNZia0J1', 'nick_name': '세미콘 네트웍스', 'comment_count': 27, 'sympathy': 515, 'not_sympathy': 160, 'report_count': None}]
        )

    @app.route ("/data", methods = ["GET"])
    def data (was):
        return was.API (result = 'ok')

    @app.route ('/webpush', methods = ["GET"])
    def webpush (was):
        return was.render ('auth/webpush.j2')

    @app.route ('/webpush/tokens', methods = ["PUT", 'OPTIONS'])
    def webpush_tokens (was, token):
        msg = messaging.Message(data={'title': 'Test'}, token=token)
        return was.API (result = messaging.send(msg))
