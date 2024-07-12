import socket

ip = "127.0.0.1"

ports=[22,80,443]

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip,port))
    if result == 0:
        print(f"Le port {port} est ouvert")
    else:
        print(f"Le port {port} n'est pas ouvert")
    sock.close()