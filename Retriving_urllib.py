# Code reads the 'romeo.txt' using URLLIB
import urllib.request
import urllib.parse
import urllib.error


mysock = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in mysock:
    line = line.decode().strip()
    print(line)
    if len(line) == 0:
        break
