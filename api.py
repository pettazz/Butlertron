import logging
import tornado.auth
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import os, os.path
import uuid
import importlib

from tornado.options import define, options

import locale
from core.strings import STRINGS
STRINGS = STRINGS[locale.getdefaultlocale()[0]]

define("port", default=8888, help="run on the given port", type=int)


class ButlertronAPI(tornado.web.Application):
    def __init__(self):
        handlers = [
            #(r"/", MainHandler),
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




class UnrecognizedEventError(Exception):
    pass


def update_handlers():
    for handler_file in os.listdir('event_handlers'):
        if handler_file.endswith('_handler.py'):
            handler_module = handler_file.split('.py', 1)[0]
            handler_short_name = handler_file.split('_handler.py', 1)[0]
            handler_class_name = "%sEventHandler" % handler_short_name.capitalize()
            # try:
            exec('from event_handlers.%s import %s' % (handler_module, handler_class_name))
            # importlib.import_module(handler_class_name, 'event_handlers.' + handler_module)
            # except:
            #     print "cant load " + handler_class_name


def main():
    tornado.options.parse_command_line()
    app = ButlertronAPI()
    update_handlers()
    
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()