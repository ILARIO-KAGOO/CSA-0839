
price =list(map(int,input().split()))

n = len(price)
p = [0]*n
m = price[n-1]
 
for i in range(n-2, 0, -1):
  if price[i] > m:
    m = price[i]
  p[i] = max(p[i+1], m - price[i])
 
min_price = price[0]
 
for i in range(1, n):
  if price[i] < min_price:
    min_price = price[i]
  p[i] = max(p[i-1], p[i]+(price[i]-min_price))
 
result = p[n-1]
print(f"Maximum profit: {result}")