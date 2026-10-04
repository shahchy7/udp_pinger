from socket import *

server_sd = socket(AF_INET, SOCK_DGRAM)

server_sd.bind(('127.0.0.1', 12000))

print("UDP server is running on 127.0.0.1:12000")

while True:
    message, client_addr = server_sd.recvfrom(1024)

    print("Received:", message.decode())

    server_sd.sendto(message, client_addr)
