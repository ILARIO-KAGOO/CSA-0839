n = int(input("Enter row: "))

for i in range(1, n+1):
  for space in range(1, n-i+1):
    print(" ",end="")
  for j in range(0,i):
    print(i-j,end=" ")
  print("\n")
