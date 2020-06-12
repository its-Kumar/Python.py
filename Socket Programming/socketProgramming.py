import socket

host = "localhost"
port = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
print("Server listning on port : ", port)
s.listen(1)
c, addr = s.accept()

print("Connection from : ", str(addr))

c.send(b"Hello, How r you?")
c.send("bye".encode())
c.close()
