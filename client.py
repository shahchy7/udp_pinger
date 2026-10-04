from socket import *
import time

def main():

    # Create UDP socket
    client_sd = socket(AF_INET, SOCK_DGRAM)

    # h2's IP address
    server_ip = '10.0.0.2'
    port = 12000

    # Wait maximum 1 second for a reply
    client_sd.settimeout(1.0)

    # Send 10 pings
    for seq in range(1, 11):

        start_time = time.time()

        message = "Ping " + str(seq) + " " + str(start_time)

        try:
            # Send message to h2
            client_sd.sendto(
                message.encode(),
                (server_ip, port)
            )

            # Wait for server's reply
            received_line, server_addr = client_sd.recvfrom(1024)

            end_time = time.time()

            # Calculate Round Trip Time
            rtt = end_time - start_time

            print(
                "Reply from",
                server_addr[0] + ":",
                received_line.decode()
            )

            print("RTT:", rtt, "seconds")

        except timeout:
            print("Request timed out")

    client_sd.close()


if __name__ == '__main__':
    main()
