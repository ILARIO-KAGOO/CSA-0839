s = list(input("Enter string: "))

if "/" in s:
  d = s.index("/")
  s[d-1] = f"{int((int(s[d-1])/int(s[d+1])))}"
  del s[d:d+2]

if "+" in s:
  d = s.index("+")
  s[d-1] = f"{int(int(s[d-1])+int(s[d+1]))}"
  del s[d:d+2]

if "-" in s:
  d = s.index("-")
  s[d-1] = f"{int(int(s[d-1])+int(s[d+1]))}"
  del s[d:d+2]

if "*" in s:
  d = s.index("*")
  s[d-1] = f"{int(int(s[d-1])+int(s[d+1]))}"
  del s[d:d+2]
print(s)