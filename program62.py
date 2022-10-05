l = [4,54,29,71,7,59,98,23]
composite = 0
prime = 0

# while True:
#   s = input()
#   if s == '*':
#     break
#   else:
#     l.append(int(s))

for i in l:
  for j in range(2,i):
    if i%j==0:
      composite+=1
      break
    elif (j==i-1):
      prime+=1

print(f"Prime: {prime} \nComposite: {composite}")
