import socket
import time

#Connecting to the server
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b''  # Variable will be stored as bytes 

#Receiving image in 5120 bytes per time and putting into a byte variable
while True:
    data = mysock.recv(5120)
    if len(data) <  1: break
    picture = picture + data
mysock.close()

#Finding the end of the header and taking it away from the image
pos = picture.find(b'\r\n\r\n')

#Selecting only the picture and saving into a JPG file
picture = picture[pos+4:]
fhand = open('stuff.jpg','wb')
fhand.write(picture)
fhand.close()
