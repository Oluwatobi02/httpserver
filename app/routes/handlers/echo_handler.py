from app.request import Request
from app.response import Response
def make_process_echo():
    def process_echo(request: Request):
        path = request.get_url().split('/')[1:][1]
        response = Response()
        response.set_header('Content-Type', 'text/plain')
        response.set_header('Connection', 'keep-alive')
        response.set_header('Content-Length', str(len(path)))
        response.set_body(path)
        return response.format_response()
    return process_echo