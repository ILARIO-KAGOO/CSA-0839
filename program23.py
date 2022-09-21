str = []
n=[]

while True:
  s = input()
  if s =='*':
    break
  else:
    str.append(int(s))

for i in range(0,len(str)):
  for j in range(0,len(str)):
    if str[i]==str[j] and i<j:
      n.append((i,j))

print(f"There are {len(n)} good pairs: {n}")
