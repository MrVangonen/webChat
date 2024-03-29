import socket
import time

host = 'localhost'
port = 9090

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

quitting = False
print ("Server Started.")

while not quitting:
    try:
        data, addr = s.recvfrom(1024)

        if addr not in clients:
            clients.append(addr)

        print(time.ctime(time.time()) + str(addr) + ": :" + str(data))

        for client in clients:
            s.sendto(data, client)
    except:
        print("Server Closed")
        quitting = True
s.close()