from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor

import json, urlparse

class SMSAPIHandler(Resource):
    def __init__(self):
        Resource.__init__(self)

    def render_POST(self, request):
        data = urlparse.parse_qs(request.content.getvalue(), True)
        msg_from = data['From'][0]
        msg_to = data['To'][0]
        msg_body = data['Body'][0]
        return '<?xml version="1.0" encoding="utf-8" ?><Response />'

class VoiceAPIHandler(Resource):
    def __init__(self):
        Resource.__init__(self)

    def render_POST(self, request):
        return '<?xml version="1.0" encoding="utf-8" ?><Response />'

class GenericAPIHandler(Resource): 
    def __init__(self):
        Resource.__init__(self)

    def render_POST(self, request):
        data = json.loads(request.content.getvalue())
        return "<html><body>HEY EVERYBODY! GENERIC API HANDLER HERE. I DON'T DO ANYTHING. <br /><pre>%s</pre></body></html>" % data

class EventHookHandler(Resource):
    def __init__(self):
        Resource.__init__(self)

    def render_POST(self, request):
        return 'wat?'


class APIDispatcher(Resource):
    def getChild(self, name, request):
        print request.__dict__
        #stupid sexy flanders

        if name == 'sms':
            return SMSAPIHandler()
        elif name == 'voice':
            return VoiceAPIHandler()
        elif name == 'event':
            return EventHookHandler()
        else:
            return GenericAPIHandler()

root = APIDispatcher()
factory = Site(root)
reactor.listenTCP(8880, factory)
reactor.run()