s = input("Enter a string: ")
l = []
ds = []
for i in range(len(s)):
  for j in range(len(s)):
    for k in range(len(s)):
      if i!=j and j!=k and k!=i:
        l.append(int(f"{s[i]}{s[j]}{s[k]}") )

for i in l:
  if l.count(i)>=2:
    ds.append(i)

print(ds)