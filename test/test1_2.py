l =[]
list = [0,0]

def sumsquare(l):
  for i in l:
    if i%2==0:
      list[0]+=i**2
    else:
      list[1]+=i**2

n = int(input("Enter no of elements: "))

if n>0:
  for i in range(0,n):
    l.append(int(input("Enter the number: ")))
  sumsquare(l)
else:
  raise ValueError("please enter positive integer")


print(f"List{list}")

