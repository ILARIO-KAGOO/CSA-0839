n = int(input())
for i in range(1,n*2+1):
  if i<=n:
    print('* '*i,end="\n")
  elif i>n:
    print('* '*(n*2-i),end="\n")