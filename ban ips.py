from scapy.all import *

# Define the list of IP addresses to block
blocked_ips = ['X.X.X.X', 'X.X.X.X']

# Define the callback function to handle incoming packets
def handle_packet(packet):
    ip = packet.getlayer(IP)
    if ip and ip.src in blocked_ips:
        print(f"Blocking packet from {ip.src}")
        packet.drop()

# Start sniffing incoming traffic
sniff(prn=handle_packet)
