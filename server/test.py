import tornado
from tornado.websocket import WebSocketHandler


class SocketHandler(WebSocketHandler):

    users = set()  # 用来存放在线用户的容器

    def open(self):
        self.users.add(self)  # 建立连接后添加用户到容器中
        for u in self.users:  # 向已在线用户发送消息
            u.write_message("hello")

    def on_message(self, message):
        for u in self.users:  # 向在线用户广播消息
            u.write_message(u"hello2")

    def on_close(self):
        self.users.remove(self)  # 用户关闭连接后从容器中移除用户
        for u in self.users:
            u.write_message("ffffff")

    def check_origin(self, origin):
        return True  # 允许WebSocket的跨域请求


settings = {
    "cookie_secret": b'*\xc4bZv0\xd7\xf9\xb2\x8e\xff\xbcL\x1c\xfa\xfeh\xe1\xb8\xdb\xd1y_\x1a',
    "template_path": "server/templates",
    "static_path": "server/static",
    "debug": False
}

app = tornado.web.Application(
    [(r"/chat", SocketHandler)], **settings
)
http_server = tornado.httpserver.HTTPServer(app)
http_server.listen(5000)
tornado.ioloop.IOLoop.current().start()
