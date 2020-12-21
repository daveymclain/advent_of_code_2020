import re

txt = "baaaba"

#Check if the string contains either "falls" or "stays":

x = re.fullmatch("b((aa|bb)(ab|ba)|(ab|ba)(aa|bb))a", txt)

print(x)

# for i in x:
#   print(i)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
