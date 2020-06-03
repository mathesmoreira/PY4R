#This program work well in a HTML well formatted
import urllib.request, urllib.parse, urllib.error
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Link where the search will be done
Enter_link = input( 'Enter link -')

#Establishing connection with the link and reading it
html = urllib.request.urlopen(Enter_link).read()

#Using Regular Expressions to search for links
links = re.findall(b'href="(http[s]?://.*?)"', html)

#Printing the links
for link in links:
    print(link.decode())