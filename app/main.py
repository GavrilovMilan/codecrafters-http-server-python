import socket


HTTP_200 = "HTTP/1.1 200 OK\r\n\r\n".encode()
HTTP_404 = "HTTP/1.1 404 Not Found\r\n\r\n".encode()
def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    # server_socket.accept()

    conn, addr = server_socket.accept()
    data = conn.recv(1024).decode()
    path = data.split()[1]
    print(data)  # b'GET / HTTP/1.1\r\nHost: localhost:4221\r\nUser-Agent: Go-http-client/1.1\r\nAccept-Encoding: gzip\r\n\r\n'
    print(path)

    if path == '/':
        conn.send(HTTP_200)
    else:
        conn.send(HTTP_404)

    server_socket.close()

if __name__ == "__main__":
    main()
