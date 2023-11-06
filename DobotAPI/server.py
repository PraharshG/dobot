import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8888))
server_socket.listen(1)
print('Server started. Waiting for incoming connections...')
index = 0
x = 0

while True:
    client_socket, client_address = server_socket.accept()
    print(f'Client connected: {client_address}')

    # Receive index request from the client
    index = client_socket.recv(1024).decode()

    if index != 0:
        x = 1
        client_socket.send(x.encode())
        client_socket.close()
