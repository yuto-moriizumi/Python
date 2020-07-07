import socket

address = ("localhost", 12345)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server.bind(address)

server.sendto(b"Hi!", address)
data, client = server.recvfrom(4096)
print(client, data)
server.close()
