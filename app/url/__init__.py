class URL:
    def __init__(self,url):
        self.url = url
        self.url_parts = self.url.split('/')[1:]

    def get_url(self):
        return self.url
