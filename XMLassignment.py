import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input()


file = urllib.request.urlopen(url).read()

sum = 0

stuff=ET.fromstring(file)
counts = stuff.findall('.//count')

for count in counts:
    sum += int(count.text)

print(sum)


#print('User count:',len(counts))
