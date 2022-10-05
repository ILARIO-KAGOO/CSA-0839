def fact(n):
  if n==1:
    return 1
  else:
    return n*fact(n-1)

x = int(input("N = "))
s = [d for d in range(1,x+1) if x%d==0]
print(f"Factorial: {fact(x)}")
print(f"Factors of {x}: {len(s)}")