import socket

HOST = "127.0.0.1"
PORT = 5001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

print("Connected to the network!")
print("Type 'exit' to stop.")

while True:
    message = input("\nEnter message: ")

    if message.lower() == "exit":
        break

    client.sendall(message.encode())

client.close()