import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input()
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')     #parser removes the ugly stuff from the html

#retrive all the anchor tabs

tags = soup('a')
#tags = soup('span')

#sum = 0
#for tag in tags:
#      sum=sum+int(tag.contents[0])
#print(sum)
for tag in tags:
   print(tag.get('href', None))

#nabeeha 

#http://py4e-data.dr-chuck.net/known_by_Jorji.html
#http://py4e-data.dr-chuck.net/known_by_Amelka.html
#http://py4e-data.dr-chuck.net/known_by_Tarik.html
#http://py4e-data.dr-chuck.net/known_by_Emma.html
#http://py4e-data.dr-chuck.net/known_by_Louise.html
#http://py4e-data.dr-chuck.net/known_by_Liberty.html