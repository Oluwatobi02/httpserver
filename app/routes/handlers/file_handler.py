from app.request import Request
from app.response import Response
def make_file_handler():
    def process_file(request: Request):
        try:
            file_path = request.get_url().split('/')[1:][1]
            print(file_path)
            response = Response()
            response.set_header('Content-Type', 'text/plain')
            response.set_header('Connection', 'keep-alive')
            with open(file_path, 'r') as file:
                print(file.read())
                response.set_body(file.read())
                response.set_header('Content-Length', str(len(response.get_body())))
                return response.format_response()

        except Exception as e:
            response = Response()
            response.set_status_code(404)
            response.set_header('Content-Type', 'text/plain')
            response.set_header('Connection', 'close')
            response.set_header('Content-Length', '0')
            return response.format_response()
    return process_file
        