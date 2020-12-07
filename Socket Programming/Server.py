import socket

# Server socket
s = socket.socket()
print("Socket Created")

# socket.bind(('IPAdress', Port No))
s.bind(("localhost", 9999))

s.listen(3)
print("Waiting for connections")

while True:
    # Accept the connection request from client
    c, addr = s.accept()

    # Recieve data from client
    name = c.recv(1024).decode()
    print("connected with ", addr, name)

    # Send data to the client
    c.send(bytes("Welcome....", "utf-8"))

    # Close the connection
    c.close()
