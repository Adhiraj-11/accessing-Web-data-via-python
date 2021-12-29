import re 

sum = 0

file = open("")

x = []
for line in file:
    a = re.findall("[0-9]+", line)
    x = x + a

for z in x:
    sum = sum + int(z)

print(sum)