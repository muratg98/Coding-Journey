from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
count = 0
numlist = list()
for tag in tags:
    # Look at the parts of a tag
    count += 1
    print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
    numbers = int(tag.contents[0])
    numlist.append(numbers)

print('Count:', count)
print("Sum:", sum(numlist))

