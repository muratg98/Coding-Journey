import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# What is the data?
while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    print('Retrieving', address)
    document = urllib.request.urlopen(address).read()
    print('Retrieved:', len(document), 'characters')
    #print(document.decode())
    tree = ET.fromstring(document)
    comments = tree.findall('comments/comment')
    print('Comments Count:', len(comments))
    numlist = list()
    for number in comments:
        number = number.find('count').text
        #print(number)
        inum = int(number)
        numlist.append(inum)
    #print(numlist)
    totalnum = sum(numlist)
    print(totalnum)