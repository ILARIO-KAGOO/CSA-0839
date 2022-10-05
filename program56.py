n = int(input("Enter no of rows: "))

s = 0.1

for i in range(0,n):
  for j in range(0,i):
    print(round(s,1),end=" ")
    s += 0.1
  s = 0.1
  print("\n")