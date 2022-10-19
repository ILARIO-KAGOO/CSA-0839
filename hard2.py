n = int(input("N = "))
l = list(map(int,input().split()))
l1 = list(map(int,input().split()))
ld = []
d = 0 
for i in range(n):
	d +=(l[i] - l1[i])
	ld.append(d)
print(max(ld))