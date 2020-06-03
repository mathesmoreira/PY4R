import urllib.request, urllib.parse, urllib.error
import json as j

fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_527570.json').read()
counts = j.loads(fhand)

comments = counts['comments']
soma= 0
for count in comments:
    conta = count['count']
    soma = soma + conta
print(soma)
