from basehandler import BaseHandler

class SmsEventHandler(BaseHandler):
    def write_error(status_code, **kwargs):
        pass

    def post(self):
        event_id = self.get_argument("event_id", default=None)
        workflow_id = self.get_argument("workflow_id", default=None)