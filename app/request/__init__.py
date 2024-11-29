from app.httpmessage import HTTPMessage

class Request(HTTPMessage):
    def __init__(self, gen_info={}, header_info={}, body={}):
        super().__init__(gen_info, header_info, body)

    def __repr__(self):
        print(self.format_response())
    