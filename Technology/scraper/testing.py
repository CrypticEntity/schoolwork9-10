import urllib.request
import re
import sys
import find 

foundAllSubURLs = 0
httpCheck = -1

while httpCheck != 0:
    url = input('Enter URL: ')
    httpCheck = url.find('http')
    if httpCheck == 0:
        print('Try again')
        print('example: https://google.com')
        print(httpCheck)

print('That is a URL')
print(httpCheck)
#request = urllib.request.urlopen(url)

#response = request.read()

filter = re.findall()

print(response)