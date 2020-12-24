import re

txt = ".############"

#Check if the string contains either "falls" or "stays":

x = re.finditer("(#).{2}(#)", txt)

print(x)

for i in x:
  print(i)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


