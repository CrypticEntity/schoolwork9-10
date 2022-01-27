import urllib.request
import re
import sys
import find 

foundAllSubURLs = 0
httpCheck = -1
httpsCheck = -1

while httpCheck != 0  and httpsCheck != 0:
    url = input('Enter URL: ')
    httpCheck = url.find('http://')
    httpsCheck = url.find('https://')
    if httpCheck != 0:
        print('Try again')
        print('example: https://google.com')

print('That is a URL')

request = urllib.request.urlopen(url)

response = request.read()

print(response)