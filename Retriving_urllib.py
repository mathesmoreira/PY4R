#Reading the Romeo txt using URLLIB
import urllib.request, urllib.parse, urllib.error

mysock = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in mysock:
    line = line.decode().strip()
    print(line)
    if len(line) == 0: break
