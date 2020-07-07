import socket

address = ("localhost", 12345)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(address)

data, client = server.recvfrom(4096)
print(server, data)
server.sendto(b"Hi!", client)
server.close()
