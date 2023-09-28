import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    print('Retrieving', address)
    document = urllib.request.urlopen(address).read()
    print('Retrieved:', len(document), 'characters')
    data = json.loads(document)
    print('Count:', len(data))
    Totalnum = list()
    for numbers in data['comments']:
        #print('Number:', numbers["count"])
        number = int(numbers['count'])
        Totalnum.append(number)
    print('Sum:', sum(Totalnum))