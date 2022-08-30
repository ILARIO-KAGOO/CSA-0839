import string
import random

a=string.ascii_lowercase
d = {}

for i in range(26):
  index = random.randint(0,25)
  try:
    d[a[index]]+=1
  except KeyError:
    d[a[index]]=0
print(d)