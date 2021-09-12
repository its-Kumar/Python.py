import socket

# client socket
c = socket.socket()

# Connect with server
c.connect(("localhost", 9999))

# Send Data to server
name = input("Enter your name: ")
c.send(bytes(name, "utf-8"))

# Receive data from server
print(c.recv(1024).decode())
