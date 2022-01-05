import urllib.request, urllib.parse, urllib.error

file = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_1440158.html")
for line in file:
    print(line.decode().strip())
    

