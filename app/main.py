import socket  # noqa: F401
from app.req_parser import parse_get, parse_header

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    while True:
        server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
        conn, address = server_socket.accept() # wait for client
        message = conn.recv(8000).decode('utf-8')
        message = message.split('\n')
        get_info = parse_get(message[0])
        header_info = parse_header(message[1:-2])
        if get_info['path'] != '/':
            conn.sendall(b'HTTP/1.1 404 Not Found\r\n\r\n')
        else:
            conn.sendall(b'HTTP/1.1 200 OK\r\n\r\n')



if __name__ == "__main__":
    main()
