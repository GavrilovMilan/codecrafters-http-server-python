import socket


HTTP_200 = "HTTP/1.1 200 OK\r\n\r\n".encode()
HTTP_404 = "HTTP/1.1 404 Not Found\r\n\r\n".encode()
def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)

    conn, addr = server_socket.accept()
    data = conn.recv(1024).decode()
    path = data.split()[1]
    string = path.split('/')[2]
    print(string)
    if path == '/':
        conn.send(HTTP_200)
    elif path.split('/')[1] == 'echo':
        conn.send(HTTP_200, string.encode())

    server_socket.close()

if __name__ == "__main__":
    main()
