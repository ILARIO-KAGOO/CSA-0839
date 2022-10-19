def delchar(str1,n1):
  li = list(str1)
  for i in li:
    if i == n1:
      li.remove(n1)
  return ''.join(e for e in li)

str2 = input("Enter string: ")
n2 = input("Enter character to be delete: ")
print(F"String after the charcter is removed: {delchar(str2,n2)}")
