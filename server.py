from socket import *
def main():
	#create a udp socket with SOCK_DGRAM
	server_sd = socket(AF_INET, SOCK_DGRAM)
	port = 12000
	server_ip = '127.0.0.1'

	#bind the address to the socket
	server_sd.bind((server_ip, port))
	print(f"UDP server is listening on {server_ip} port {port}")

	#server keeps listening forever
	while True:
		#read data and the sender's address (no connection in UDP)
		received_line, client_addr = server_sd.recvfrom(1024)
		print(f"Received: {received_line.decode()} from {client_addr}")

		#echo the same data back to the client's address
		server_sd.sendto(received_line, client_addr)

if __name__ == '__main__':
	main()