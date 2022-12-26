#!/usr/bin/env python3
import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 8888 

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((bind_ip, bind_port))
print(f"[*] Listening on {bind_ip}:{bind_port}")

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(f"[*] Received: {request}")
    client_socket.send("ACK!")
    client_socket.close()

while True:
    client, addr = server.recvfrom(1024)
    print(f"[*] Accepted connection from: {addr[0]}:{addr[1]}")

