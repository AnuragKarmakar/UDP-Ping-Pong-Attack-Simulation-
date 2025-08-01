
#Anurag's Victim

import socket

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a UDP socket
udp.bind(("0.0.0.0", 9090))  # Bind to all available network interfaces on port 9090

print("Waiting for UDP packets...")

try:
    while True:
        data, (ip, port) = udp.recvfrom(1024)  # Receive data from any sender
        print("Received from {}:{} | {}".format(ip, port, data.decode('utf-8', 'ignore')))
        
        # Send a response back to the sender
        anurag = b'Victim-Ping\n'
        udp.sendto(anurag, (ip, port))
        print(f"Sent response to {ip}:{port}")
except KeyboardInterrupt:
    print("\nServer shutting down gracefully.")
    udp.close()
except Exception as e:
    print(f"Error: {e}")
    udp.close()

