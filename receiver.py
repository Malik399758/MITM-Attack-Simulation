print("Receiver program started!")

import socket

HOST = "127.0.0.1"
PORT = 5002

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen(1)

print("Receiver is waiting for connection...")

connection, address = server.accept()

print("Connected:", address)

while True:
    data = connection.recv(1024)

    if not data:
        break

    print("Receiver received:", data.decode())

connection.close()
server.close()