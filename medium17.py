s1 = input()
s2 = input()
def matc(s,s3):
  count = 0
  l = s if len(s)<=len(s3) else s3
  a = s3 if l==s else s
  for i in range(len(a)): 
    if l[i] == a[i]: count+=1
  return count
print(matc(s1,s2))