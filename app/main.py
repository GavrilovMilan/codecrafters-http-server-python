import socket


_HTTP_200_RESP = "HTTP/1.1 200 OK\r\n\r\n".encode()
def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    server_socket.accept()
    print('Stage 1 Zavrsen')
    (conn, address) = server_socket.accept()
    print('1')
    data = conn.recv(1024)
    print('2')
    print(data)
    conn.send(_HTTP_200_RESP)
    conn.close()


if __name__ == "__main__":
    main()
