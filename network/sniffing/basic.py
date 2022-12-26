#!/usr/bin/env python3
import socket

host = "192.168.0.196"

socket_protocol = socket.IPPROTO_ICMP
sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol) 
sniffer.bind((host, 0))

# we want the IP headers included in the capture
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# read in a single packet
print(sniffer.recvfrom(65535))
   
