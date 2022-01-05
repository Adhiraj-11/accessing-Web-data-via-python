import urllib.request, urllib.parse, urllib.error
import json
from xml.etree.ElementTree import Comment

sum = 0

url = input()
file = urllib.request.urlopen(url).read()

x = json.loads(file)


for item in x["comments"]:
	number = int(item["count"])
	sum = sum + number

print(sum)


# info=json.loads(url)
# print('User count:',len(info))

