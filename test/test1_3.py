str = []
maxi = 0

print("Enter the strings (* to quit): ")
while True:
  s = input()
  if s =='*':
    break
  else:
    str.append(s)

for i in str:
  s = i.split(" ")
  n = len(s)
  maxi = max(maxi,n)

print(f"{maxi} maximum no of words in the sentence.")
