IP Blocker using Scapy

This script utilizes the Scapy library to sniff incoming network traffic and block packets from specified IP addresses.
Requirements

    Python
    Scapy library

Installation

    Ensure you have Python installed on your system.
    Install Scapy:

    bash

    pip install scapy

Usage

    Edit the blocked_ips list in the script to include the IP addresses you wish to block.

    python

blocked_ips = ['X.X.X.X', 'X.X.X.X']

Replace X.X.X.X with the actual IP addresses.

Run the script with administrative privileges (required for packet manipulation):

bash

    sudo python3 script_name.py

    The script will start sniffing incoming traffic. If a packet from a blocked IP address is detected, it will print a message indicating that the packet is being blocked.

Note

This script provides a basic demonstration of using Scapy to block specific IP addresses. In a real-world scenario, you might want to consider more comprehensive solutions or firewalls for blocking unwanted traffic.
