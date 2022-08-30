l = []
n = int(input())
k = int(input())
print(n,k)
if k%2==0:
  for i in range(n):
    if i == 0 or i%2==0:
      l.append(1)
    else:
      l.append(0)
else:
  for i in range(n):
    if i == 0 or i%2==0:
      l.append(0)
    else:
      l.append(1)
print(l,end=" ")