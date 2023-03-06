import socket


def server_program():
    hostname = socket.gethostname()
    port = 6000

    second_socket_server = socket.socket()
    second_socket_server.bind((hostname, port))

    second_socket_server.listen(1)

    conn, address = second_socket_server.accept()

    print("Connection from: " + str(address))
    conn.send("Hello, I'm second echo server.".encode())

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + data)
        conn.send(data.encode())

    conn.close()


if __name__ == '__main__':
    server_program()