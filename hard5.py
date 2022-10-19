s1 = list(input("S1 = ").split())
s2 = list(input("S2 = ").split())
for i in s1:
  for j in s2:
    if i == j:
      s1.remove(i)
      s2.remove(i)
s1 = "".join(s1)
s2 = "".join(s2)
print(f"{s1} \n{s2}")