from app.request import Request
from app.response import Response
def make_process_user_agent():
    def process_user_agent(request: Request):
        user_agent = request.get_headers().get('User-Agent', 'Not there')
        response = Response()
        response.set_header('Content-Type', 'text/plain')
        response.set_header('Connection', 'keep-alive')
        response.set_header('Content-Length', str(len(user_agent)))
        response.set_body(user_agent)
        return response.format_response()
    return process_user_agent