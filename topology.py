from mininet.net import Mininet
from mininet.node import OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink

def main():

    # Create Mininet
    net = Mininet(
        switch=OVSSwitch,
        link=TCLink
    )

    print("Creating hosts...")

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

    print("\n================================")
    print("Mininet network started!")
    print("================================")
    print("h1 IP: 10.0.0.1")
    print("h2 IP: 10.0.0.2")
    print("UDP server port: 12000")
    print("================================\n")

    # Test connectivity
    print("Testing connection between h1 and h2...\n")

    result = h1.cmd('ping -c 2 10.0.0.2')

    print(result)

    # Start server on h2
    print("Starting UDP server on h2...\n")

    h2.cmd('python3 server.py > server_output.txt 2>&1 &')

    # Give server a moment to start
    import time
    time.sleep(1)

    # Start client on h1
    print("Starting UDP client on h1...\n")

    client_output = h1.cmd('python3 client.py')

    print("================================")
    print("CLIENT OUTPUT")
    print("================================")

    print(client_output)

    # Show server output
    print("================================")
    print("SERVER OUTPUT")
    print("================================")

    server_output = h2.cmd('cat server_output.txt')

    print(server_output)

    # Open Mininet CLI
    print("================================")
    print("Entering Mininet CLI")
    print("Type 'exit' to finish.")
    print("================================\n")

    CLI(net)

    # Stop network
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    main()
