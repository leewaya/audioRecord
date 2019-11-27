# -*- coding: utf-8 -*-
import os.path
import tornado
import tornado.websocket
from tornado.web import Application, RequestHandler

class IndexHandler(RequestHandler):
    def get(self):        
        self.render("index.html")
        
class webRTCServer(tornado.websocket.WebSocketHandler):
    # 用户集合
    users = set()

    def open(self):
        # 连接建立时往房间添加用户
        print("open") 
        self.users.add(self)

    def on_message(self, message):        
        # 接收到消息时进行广
        print("on_message")
        for user in self.users: 
            user.write_message(message, binary=True)

    def on_close(self):
        # 链接断开时移除用户
        print ("on_close")
        self.users.remove(self)

    def check_origin(self, origin):
        # 允许跨域访问
        print ("check_origin") 
        return True


if __name__ == '__main__':
    # 定义路由
    app = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/webrtc", webRTCServer),
        ],
        
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True
    )

    # 启动服务器
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.current().start()