import socket
from app.formatter import parse_get, parse_header
from app.request import Request
from app.response import Response
def handle_connections(client : socket.socket, address):
    while client:
        try:
            message = client.recv(8000).decode('utf-8')
        except Exception as e:
            client.send(b'HTTP/1.1 400 Bad Request\n\n')
        
        message = message.split('\n')
        get_info = parse_get(message[0])
        header_info = parse_header(message[1:-2])
        body = message[-1]
        request = Request(get_info, header_info, body)
        path = request.get_url().split('/')[-1]
        print(request.get_url())

        try:
            response = Response()
            response.set_gen_info(get_info)
            response.set_header('Content-Type', 'text/plain')
            response.set_header('Content-Length', str(len(path)))
            response.set_header('Connection', 'keep-alive')
            response.set_body(path)
            client.send(response.format_response())
        except Exception as e:
            print(f"Error handling request: {e}")
            # break
    # client.close()