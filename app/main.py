import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    server_socket.accept()

    connect, address = server_socket.accept()  # wait for client
    if connect:
        connect.recv(4096)
        ok = "HTTP/1.1 200 OK\r\n\r\n"
        connect.sendall(ok.encode())
        connect.close()

    # conn, addr = server_socket.accept()
    # data = conn.recv(1024)
    # conn.send("HTTP/1.1 200 OK\r\n\r\n".encode())
    # server_socket.close()

if __name__ == "__main__":
    main()
