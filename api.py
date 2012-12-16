import logging
import tornado.auth
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import os.path
import uuid

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/event", EventHandler),
            # (r"/auth/login", AuthLoginHandler),
            # (r"/auth/logout", AuthLogoutHandler),
        ]
        settings = dict(
            # cookie_secret="131afe2b2ce8ea020b79c75e52a3d2aa",
            # login_url="/auth/login",
            # template_path=os.path.join(os.path.dirname(__file__), "templates"),
            # static_path=os.path.join(os.path.dirname(__file__), "static"),
            # xsrf_cookies=True,
            # autoescape="xhtml_escape",
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class BaseHandler(tornado.web.RequestHandler):
    pass


class MainHandler(BaseHandler):
    # / will be the webapp i think, so these are pointless here
    def get(self):
        self.write({'what': 'idunno'})

    def post(self):
        self.write({'what': 'idunno'})

class EventHandler(BaseHandler):
    def post(self):
        workflow_id = self.get_argument("workflow_id")



def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()