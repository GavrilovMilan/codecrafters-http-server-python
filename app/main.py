import socket
import threading
import os
import sys


HTTP_200 = "HTTP/1.1 200 OK\r\n"
HTTP_404 = "HTTP/1.1 404 Not Found\r\n\r\n"

def handle_request(conn):
    data = conn.recv(1024).decode()
    path = data.split()[1]
    string = ''.join(path[6:])
    # print(data)
    if path == '/':
        conn.send((HTTP_200 + '\r\n').encode())
    elif path.split('/')[1] == 'echo':
        conn.send(
            (HTTP_200 + 'Content-Type: text/plain\r\n' + f'Content-Length: {len(string)}\r\n\r\n' + string).encode())
    elif path.split('/')[1] == 'user-agent':
        agent = data.split('\r\n')[2].split()[1]
        # print(agent)
        conn.send((HTTP_200 + 'Content-Type: text/plain\r\n' + f'Content-Length: {len(agent)}\r\n\r\n' + agent).encode())
    elif path.split('/')[1] == 'files':
        filename = path.split('/')[2]
        dir = sys.argv[-1]
        if filename in dir:
            conn.send((HTTP_200 + 'Content-Type: application/octet-stream\r\n').encode())
        else:
            conn.send(HTTP_404.encode())
    else:
        conn.send(HTTP_404.encode())
    conn.close()

def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)

    while True:
        conn, addr = server_socket.accept()
        t = threading.Thread(target=handle_request, args=(conn,))
        t.start()



if __name__ == "__main__":
    main()
