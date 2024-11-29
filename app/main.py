import socket
from concurrent.futures import ThreadPoolExecutor
from app.handle_connections import handle_connections

HOST = "0.0.0.0"
PORT = 4221
MAX_WORKERS = 10  # Maximum concurrent threads


def main():
    print(f"Server started, listening on {HOST}:{PORT}")

    # Create a TCP server socket
    with socket.create_server((HOST, PORT), reuse_port=True) as server_socket:
        server_socket.settimeout(5)  # Optional timeout
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            while True:
                try:
                    # Accept a connection from a client
                    conn, address = server_socket.accept()
                    print(f"Connection received from {address}")
                    
                    # Delegate the connection to a thread
                    executor.submit(handle_connections, conn, address)
                except socket.timeout:
                    # Continue the loop after timeout
                    continue
                except Exception as e:
                    print(f"Error accepting connection: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Shutting down server gracefully")
