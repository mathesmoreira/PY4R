#Reading binary file using URLLIB

import urllib.request, urllib.parse, urllib.error

#Requesting and opening the web file
fhand = urllib.request.urlopen('https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Collage_of_Six_Cats-02.jpg/500px-Collage_of_Six_Cats-02.jpg')
size = 0 

#Writing in a JPG file
image = open('cats.jpg', 'wb') # WB argument opens a file for writing only
while True:
    #To avoid crashing situations
    info = fhand.read(10000) #Retrieving the file in blocks
    if len(info) == 0: break
    size = size + len(info)
    print(size,len(info))
    image.write(info)
