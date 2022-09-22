l = ["FizzBuzz","Fizz","Buzz"]
s=[]

n = int(input("Enter number: "))

for i in range(1,n+1):
  if i%3==0 and i%5==0:
    s.append(l[0])
  elif i%3==0:
    s.append(l[1])
  elif i%5==0:
    s.append(l[2])
  else:
    s.append(f"{i}")

print(f"\n{s}")