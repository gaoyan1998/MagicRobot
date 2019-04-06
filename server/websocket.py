from tornado.websocket import WebSocketHandler


class SocketHandler(WebSocketHandler):

    def __init__(self):
        print("")

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
