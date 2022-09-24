rows = int(input("Enter number of rows: "))
coef = 1
k = int(input("Enter the row: "))
sumi = 0
for i in range(1, rows+1):
  for space in range(1, rows-i+1):
    print(" ",end="")
  for j in range(0, i):
    if j==0 or i==0:
      coef = 1
      if i == k:
        sumi += coef
    else:
      coef = coef * (i - j)//j
      if i == k:
        sumi += coef
    print(coef, end = " ")
  print()

print(f"sum of {k} row is {sumi}")