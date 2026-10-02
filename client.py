from socket import *
import time
def main():
	#create a udp socket with SOCK_DGRAM
	client_sd = socket(AF_INET, SOCK_DGRAM)
	server_ip = '127.0.0.1'
	port = 12000

	#wait at most 1 second for a reply
	client_sd.settimeout(1.0)

	#send 10 pings with sequence numbers 1 to 10
	for seq in range(1, 10+1):
		start_time = time.time()
		message = "Ping " + str(seq) + " " + str(start_time)

		try:
			#send data to the server's address
			client_sd.sendto(message.encode(), (server_ip, port))

			#read the echoed data from the server
			received_line, server_addr = client_sd.recvfrom(1024)
			end_time = time.time()

			#rtt = time after receive - time before send
			rtt = end_time - start_time
			print(f"Reply from {server_addr[0]}: {received_line.decode()}")
			print(f"RTT: {rtt} seconds")
		except timeout:
			#no reply within 1 second
			print(f"Request timed out")

	#closing the socket
	client_sd.close()

if __name__ == '__main__':
	main()