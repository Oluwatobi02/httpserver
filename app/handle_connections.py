from app.formatter import parse_get, parse_header
def handle_connections(client, address):
    message = client.recv(8000).decode('utf-8')
    message = message.split('\n')
    get_info = parse_get(message[0])
    header_info = parse_header(message[1:-2])
    if get_info['Request URL'] != '/':
        client.sendall('HTTP/1.1 404 Not Found\r\n\r\n'.encode('utf-8'))
    else:
        client.sendall('HTTP/1.1 200 OK\r\n\r\n'.encode('utf-8'))
    client.close()