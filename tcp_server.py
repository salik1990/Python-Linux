import socket

def start_tcp_server(host='127.0.0.1', port=65432):
    """Start a TCP server that echoes received data back to the client."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen()
        print(f"Server started and listening on {host}:{port}")
        prefix = "Echo Data Back:".encode()
        while True:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"Received IP Data From TCP Client: {data.decode()}")
                    conn.sendall(prefix+data)

if __name__ == "__main__":
    start_tcp_server()
