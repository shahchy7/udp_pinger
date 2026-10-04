from socket import *
import time

def main():

    client_sd = socket(AF_INET, SOCK_DGRAM)

    server_ip = '127.0.0.1'
    port = 12000

    client_sd.settimeout(1.0)

    for seq in range(1, 11):

        start_time = time.time()

        message = "Ping " + str(seq) + " " + str(start_time)

        try:
            client_sd.sendto(
                message.encode(),
                (server_ip, port)
            )

            received_line, server_addr = client_sd.recvfrom(1024)

            end_time = time.time()

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
