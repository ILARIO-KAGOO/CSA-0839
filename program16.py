a = "idk"
b = ['a','b','c']
c = ['d','e','f']
d = ['g','h','i']
e = ['j','k','l']
f = ['m','n','o']
g = ['p','q','r','s']
h = ['t','u','v']
i = ['w','x','y','z']
dicts = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9}

n = input("Enter number: ")
l = [int(i) for i in n]
l_i=[]
for i in l:
  for j,v in enumerate(dicts):
    s = int(j)
    if i-1 == s:
      exec("%s" %v)
      l_i.append(v)

print(l_i)