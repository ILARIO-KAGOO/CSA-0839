n = int(input("Enter the no of steps: "))

def fibi(i):
  if i<=1:
    return i 
  return fibi(i-1)+fibi(i-2)

print(fibi(n+1))