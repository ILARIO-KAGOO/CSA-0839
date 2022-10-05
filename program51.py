import math as mt
x = int(input("Enter limit: "))
s = [g for g in range(1,x+1)]
sq = [g**2 for g in s]
ans = []

for i in s:
  for j in s:
    d = i**2+j**2
    if d in sq:
      l = (i,j,int(mt.sqrt(d)))
      ans.append(l)

print(ans)