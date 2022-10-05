s = float(input("Enter starting value: "))
n = int(input("Enter no of lines: "))

for i in range(0,n):
  for i in range(0,i):
    print(round(s,1),end=" ")
    s+=.1
  print("\n")