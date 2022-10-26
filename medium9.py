from itertools import product
d = {
  "1": ["infinite"],
  "2": ["a","b","c"],
  "3": ["d","e","f"],
  "4": ["g","h","i"],
  "5": ["h","k","l"],
  "6": ["m","n","o"],
  "7": ["p","q","r","s"],
  "8": ["t","u","v"],
  "9": ["w","x","y","z"],
  "*": ["+"],
  "0": ["__"],
  "#": ["idk"],
}
n = input()
l = []
ans = []

if n == "": 
  print([]) 
  exit()

for i in n:
  l.append(d[i])

if len(l) == 1:
  print(l[0])
  exit()


f = product(l[0],l[1])
for i in f: ans.append("".join(g for g in i))

print(ans)