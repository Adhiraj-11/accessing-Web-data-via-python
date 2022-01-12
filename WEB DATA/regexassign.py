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


import re
 
Substring ='string'
 
 
String1 ='''We are learning regex with everyone
         regex is very useful for string matching.
          It is fast too.'''
String2 ='''string We are learning regex with everyone
         regex is very useful for string matching.
          It is fast too.'''
 
# Use of re.search() Method
print(re.search(Substring, String1, re.IGNORECASE))
# Use of re.match() Method
print(re.match(Substring, String1, re.IGNORECASE))

import re
   
# A sample text string where regular expression 
string = """Hello my Number is 123456789 and
             my friend's number is 987654321"""
   
# A sample regular expression to find digits.
regex = '\d+'            
   
match = re.findall(regex, string)
print(match)

#re.split(pattern, string, maxsplit=0, flags=0)

#re.compile(pattern, flags=0)