import socket
import time


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    second_port = 6000

    client_socket = socket.socket()  # instantiate
    second_client_socket = socket.socket()

    client_socket.connect((host, port))  # connect to the server
    second_client_socket.connect((host, second_port))

    data = client_socket.recv(1024).decode()  # receive response
    print('Received from first server: ' + data)  # show in terminal

    data = second_client_socket.recv(1024).decode()
    print('Received from second server: ' + data)

    while True:
        message = input("> ")  # again take input
        if message.lower().strip() == 'bye':
            break
        client_socket.send(message.encode())  # send message
        second_client_socket.send(message.encode())


        while True:

            print(data)
            data = ""
            print(data)
            started_time = time.time()

            data = client_socket.recv(1024).decode()

            if len(data) != 0:
                print('Received from first server: ' + data)
                break
            else:
                curr_time = time.time()
                delay = curr_time - started_time
                print(f"Server delay: {delay}")

        while True:
            started_time = time.time()
            data = second_client_socket.recv(1024).decode()

            if data:
                print('Received from second server: ' + data)
                break
            else:
                curr_time = time.time()
                delay = int(curr_time - started_time)
                print(f"Server delay: {delay}")

    client_socket.close()  # close the connection
    second_client_socket.close()


if __name__ == '__main__':
    client_program()