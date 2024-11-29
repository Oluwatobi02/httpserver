
class Request:
    def __init__(self, get_info, header_info, body):
        self.__url = get_info['Request URL']
        self.__get_info = get_info
        self.__method = get_info['Request Method']
        self.__net_type = get_info['net_type']
        self.__header_info = header_info
        self.__body = body

    def get_url(self):
        return self.__url
    
    def get_method(self):
        return self.__method
    
    def get_net_type(self):
        return self.__net_type
    
    def get_headers(self):
        return self.__header_info
    
    def get_body(self):
        return self.__body
    
    def __repr__(self):
        return f"Request: {self.__method} {self.__url} {self.__net_type}"