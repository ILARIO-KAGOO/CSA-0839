n= []
f = []
while True:
  s = input()
  if s == "*":
    break
  else:
    n.append(s)

for i in range(0,len(n)):
  count = 0
  for j in range(0,len(n)):
    if n[i]>n[j] and i!=j:
      count += 1
  f.append(count)
  count = 0

print(f)


