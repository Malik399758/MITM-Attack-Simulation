# Read
# import socket

# HOST = "127.0.0.1"

# ATTACKER_PORT = 5001
# RECEIVER_PORT = 5002

# proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# proxy.bind((HOST, ATTACKER_PORT))
# proxy.listen(1)

# print("Attacker is waiting for Sender...")

# sender, address = proxy.accept()

# print("Sender connected:", address)

# receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# receiver.connect((HOST, RECEIVER_PORT))

# while True:
#     data = sender.recv(1024)

#     if not data:
#         break

#     message = data.decode()

#     print("[ATTACKER OBSERVED]:", message)

#     receiver.sendall(data)

# sender.close()
# receiver.close()
# proxy.close()



# Modify Message



import socket

HOST = "127.0.0.1"

ATTACKER_PORT = 5001
RECEIVER_PORT = 5002

proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy.bind((HOST, ATTACKER_PORT))
proxy.listen(1)

print("Attacker waiting for Sender...")

sender, address = proxy.accept()

print("Sender connected!")

receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver.connect((HOST, RECEIVER_PORT))

while True:

    data = sender.recv(1024)

    if not data:
        break

    message = data.decode()

    print("\nOriginal message:", message)

    modified_message = input(
        "Attacker: Enter modified message: "
    )

    print("Sending modified message:", modified_message)

    receiver.sendall(modified_message.encode())

sender.close()
receiver.close()
proxy.close()



