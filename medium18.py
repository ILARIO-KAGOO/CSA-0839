n = int(input())
fact = 1
nf = 0
for i in range(1,n+1):
  fact*=i
for i in range(1,n+1):
  if n%i == 0:
    nf+=1
print(f"{n} Factorial: {fact}\nno of factors for {n}: {nf}")