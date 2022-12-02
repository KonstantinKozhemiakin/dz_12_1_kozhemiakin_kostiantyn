import socket
import asyncio

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 55000
socket_server.connect((server_host, sport))

while True:
    message = input("Me : ")
    socket_server.send(message.encode())
    message = (socket_server.recv(1024)).decode()
    print('Server: ', message)
socket_server.close()
