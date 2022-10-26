a = list(map(int,input().split()))
l = 0
r = len(a)-1
area = 0

while l<r:
  area = max(area,min(a[l],a[r])*(r-l))
  if a[l]<a[r]:
    l+=1
  else:
    r-=1

print(f"The largest area is {area}")