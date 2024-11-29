from app.httpmessage import HTTPMessage
from app.url import URL
# inheriting from HTTPMessage
class Response(HTTPMessage):
    def __init__(self, gen_info={}, header_info={}, body=""):
        super().__init__(gen_info, header_info, body)
        

    def set_gen_info(self, gen_info):
        self.gen_info = gen_info
        self.method = gen_info.get('Request Method', 'UNKNOWN')

    def _set_headers(self, headers):
        self.headers = headers
        return self

    def __repr__(self):
        return self.format_response()
    
    def set_header(self, key, value):
        self.headers[key] = value
        return self
    
    def set_url(self, url):
        self.url = URL(url)
        return self
    
    def set_body(self, body):
        self.body = body
        return self
    
    