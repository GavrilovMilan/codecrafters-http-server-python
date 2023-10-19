import socket


HTTP_200 = "HTTP/1.1 200 OK\r\n"
HTTP_404 = "HTTP/1.1 404 Not Found\r\n\r\n"
def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)

    conn, addr = server_socket.accept()
    data = conn.recv(1024).decode()
    path = data.split()[1]
    string = ''.join(path.split('/')[2:])
    print(path)
    print(string)
    if path == '/':
        conn.send((HTTP_200 + '\r\n').encode())
    elif path.split('/')[1] == 'echo':
        conn.send((HTTP_200 + 'Content-Type: text/plain/r/n' + f'Content-Length: {len(string)}\r\n\r\n' + string).encode())
    else:
        conn.send(HTTP_404.encode())

    server_socket.close()

if __name__ == "__main__":
    main()
