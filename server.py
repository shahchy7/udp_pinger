from socket import *

server_sd = socket(AF_INET, SOCK_DGRAM)

# Listen on port 12000 on all network interfaces
server_sd.bind(('0.0.0.0', 12000))

print("UDP Server is running on port 12000...")

while True:
    message, client_addr = server_sd.recvfrom(1024)

    print("Received:", message.decode())
    print("From:", client_addr)

    # Send the same message back to the client
    server_sd.sendto(message, client_addr)
