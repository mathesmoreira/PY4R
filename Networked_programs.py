# Programa acessa um website e pega uma imagem
# dele, salvando em um arquivo 'stuff2.jpg'

import socket
import time


HOST = 'data.pr4e.org'
PORT = 80

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""  # stored as a bytes objects

while True:
    data = mysock.recv(5120)
    if len(data) < 1:
        break
    time.sleep(0.25)
    count = count + len(data)
    print(len(data), count)
    picture = picture + data
mysock.close()

# Look for the end of the header (2 CRLF)
pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())
print(pos)

# Skip past the header and save the picture data
picture = picture[pos+4:]  # +4 devido ao /r/n/r/n(linha em branco)
fhand = open("stuff2.jpg", "wb")
fhand.write(picture)
fhand.close()
