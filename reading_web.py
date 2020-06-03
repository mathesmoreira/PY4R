import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)


for line in cmd:
    line = mysock.recv(512)
    line = line.decode().strip()
    if len(line) == 0:
        break
    print(line)
