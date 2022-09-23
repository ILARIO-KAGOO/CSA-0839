n= []
si = []
print("Enter the number(* to quit): ")
while True:
  s = input()
  if s == "*":
    break
  else:
    n.append(int(s))

for i in range(0,len(n)):
  count = 0
  for j in range(0,len(n)):
    if n[i]>n[j] and i!=j:
      count += 1
  si.append(count)
  count = 0

print(si)