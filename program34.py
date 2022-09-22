s = input("Enter string: ")
a = s.lower()
h = ''

for i in a:
  if i.isalnum():
    h+=i
  else:
    continue

if h == h[::-1]:
  print(f"Its a palindrome")
else:
  print(f"Its not a palindrome")
