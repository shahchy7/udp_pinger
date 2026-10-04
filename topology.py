from mininet.net import Mininet
from mininet.node import OVSController
from mininet.cli import CLI
from mininet.log import setLogLevel
import time


def create_topology():

    # Create Mininet
    net = Mininet(controller=OVSController)

    print("\nCreating Mininet topology...")

    # Create two hosts
    h1 = net.addHost('h1', ip='10.0.0.1/24')
    h2 = net.addHost('h2', ip='10.0.0.2/24')

    # Create switch
    s1 = net.addSwitch('s1')

    # Connect hosts to switch
    net.addLink(h1, s1)
    net.addLink(h2, s1)

    # Start network
    net.start()

    print("\n========================================")
    print("Mininet topology started")
    print("========================================")
    print("h1 IP: 10.0.0.1")
    print("h2 IP: 10.0.0.2")
    print("========================================\n")

    # Test connectivity
    print("Testing connectivity between h1 and h2...\n")
    net.pingAll()

    print("\n========================================")
    print("Starting UDP Server on h1")
    print("Server: 127.0.0.1:12000")
    print("========================================\n")

    # Start the UDP server on h1.
    # Because the server binds to 127.0.0.1,
    # it must run on the same host as the client.
    h1.cmd(
        'python3 server.py > server_output.txt 2>&1 &'
    )

    time.sleep(1)

    print("========================================")
    print("Starting UDP Client on h1")
    print("========================================\n")

    # Run the client on h1
    client_output = h1.cmd(
        'python3 client.py'
    )

    # Display client output
    print("========== CLIENT OUTPUT ==========")
    print(client_output)

    # Display server output
    print("========== SERVER OUTPUT ==========")
    print(
        h1.cmd('cat server_output.txt')
    )

    print("========================================")
    print("UDP Pinger finished")
    print("========================================")

    # Open Mininet CLI
    CLI(net)

    # Stop network after exiting CLI
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    create_topology()
