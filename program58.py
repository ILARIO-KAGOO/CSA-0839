n = int(input("Enter the start range: "))
m = int(input("Enter the end range: "))
l = []

for i in range(n+1,m+1):
  for j in range(2,i+1):
    if i % j ==0 and i !=j and i not in l:
      l.append(i)

print(l)