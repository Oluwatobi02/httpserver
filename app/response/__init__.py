status_messages = {
    200: "OK",
    404: "Not Found",
    500: "Internal Server Error",
}

class Response:
    def __init__(self):
        self.__status_code = 200
        self._get_info = {}
        self.__headers = {}
        self.__body = ""
    def _set_headers(self, headers):
        self.__headers = headers
        return self

    def __repr__(self):
        return self.format_response(self.__status_code, self.__headers, self.__body)

    def get_status_code(self):
        return self.__status_code
    
    def get_headers(self):
        return self.__headers
    
    def get_body(self):
        return self.__body
    
    def set_status_code(self, status_code):
        self.__status_code = status_code
        return self
    
    def set_header(self, key, value):
        self.__headers[key] = value
        return self
    
    def set_body(self, body):
        self.__body = body
        return self
    
    def format_response(self):

        status_message = status_messages.get(self.__status_code, "Unknown Status")

        # Format status line
        response = f"HTTP/1.1 {self.__status_code} {status_message}\r\n"

        # Add headers
        for key, value in self.__headers.items():
            response += f"{key}: {value}\r\n"

        # Add a blank line to separate headers from the body
        response += "\r\n"

        # Append the body
        response += self.__body

        return response.encode('utf-8')