from basehandler import BaseHandler

class SmsEventHandler(BaseHandler):
    BUTL_EVENT_API_PATTERNS = ['sms']

    def write_error(status_code, **kwargs):
        pass

    def post(self):
        print self.cookies
        event_id = self.get_argument("event_id", default=None)
        