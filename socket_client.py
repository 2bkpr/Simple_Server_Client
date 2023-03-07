import socket
import time
import asyncio


# async def send(socket, message):
#     start_time = time.time()
#     socket.send(message.encode())
#     await asyncio.sleep(0.1)
#     data = socket.recv(1024).decode()
#     end_time = time.time()
#     delay = end_time - start_time
#     print(f"\n delay was {delay}")
#     return data
#

def request(socket, message):
    start_time = time.time()
    socket.send(message.encode())
    data = socket.recv(1024).decode()
    end_time = time.time()
    delay = end_time - start_time
    print(f"Waited for an answer {delay} seconds")
    return data


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

        start_time = time.time()
        data_1 = request(client_socket, message)
        if len(data_1) != 0:
            print(f'Received from first server: {data_1}')

        data_2 = request(second_client_socket, message)
        if len(data) != 0:
            print(f'Received from second server: {data_2}')
        end_time = time.time()
        overall_time = end_time - start_time
        print(f'Sum time took: {overall_time}')

    client_socket.close()  # close the connection
    second_client_socket.close()


if __name__ == '__main__':
    client_program()