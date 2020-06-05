# Programa conecta,  através de comandos da biblioteca socket,
# a um server, recebe os dados e imprimi o resultado
import socket

# Connecting to a server
# Think of a socket as a file handle it doesnt have any data

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

mysock.send(cmd)

# Reading the webpage
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
