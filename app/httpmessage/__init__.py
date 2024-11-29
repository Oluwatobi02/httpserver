from app.url import URL
class HTTPMessage:
    status_messages = {
    200: "OK",
    404: "Not Found",
    500: "Internal Server Error",
}
    def __init__(self, gen_info={}, header_info={}, body=""):
        self.status_code = 200
        self.gen_info: dict = gen_info
        self.method: str = gen_info.get('Request Method', 'UNKNOWN')
        self.url = URL(gen_info.get('Request URL', ''))
        self.net_type: str = gen_info.get('net_type', 'UNKNOWN')
        self.headers = header_info
        self.body = body
    
    def get_gen_info(self):
        return self.gen_info
    def get_status_code(self):
        return self.status_code
    
    def get_url(self):
        return self.url.get_url()
    
    def get_headers(self):
        return self.headers
    
    def get_body(self):
        return self.body
    
    def get_net_type(self):
        return self.net_type
    
    def set_status_code(self, status_code):
        self.status_code = status_code
    

    def format_response(self):

        status_message = HTTPMessage.status_messages.get(self.status_code, "Unknown Status")

        # Format status line
        response = f"HTTP/1.1 {self.status_code} {status_message}\r\n"

        # Add headers
        for key, value in self.headers.items():
            response += f"{key}: {value}\r\n"

        # Add a blank line to separate headers from the body
        response += "\r\n"

        # Append the body
        response += self.body

        return response.encode('utf-8')
    
    def __str__(self):
        headers = "\r\n".join(f"{key}: {value}" for key, value in self.headers.items())
        return f"HTTP/1.1 200 OK\r\n{headers}\r\n\r\n{self.body}"