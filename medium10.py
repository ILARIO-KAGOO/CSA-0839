i = int(input("Enter number: "))

def minsquare(n):
  if n <= 3:
    return n
  
  res = n

  for x in range(1, n + 1):
    temp = x * x
    if temp > n:
      break
    else:
      res = min(res, 1 + minsquare(n - temp))
  return res

print(minsquare(i))

