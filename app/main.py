import socket


_HTTP_200_RESP = "HTTP/1.1 200 OK\r\n\r\n".encode()
def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    server_socket.accept()

    server_socket.listen(5)
    (conn, _) = server_socket.accept()
    data = conn.recv(1024)
    print(data)
    conn.send(_HTTP_200_RESP)
    conn.close()

    # with server_socket:
    #     conn, _ = server_socket.accept()  # wait for client
    #     conn.send("HTTP/1.1 200 OK\r\n\r\n".encode())


if __name__ == "__main__":
    main()
