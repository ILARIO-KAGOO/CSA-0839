def minJumps(arr, n):
  jumps = [0 for i in range(n)]
 
  if (n == 0) or (arr[0] == 0):
    return float('inf')
 
  jumps[0] = 0
 
    # Find the minimum number of
    # jumps to reach arr[i] from
    # arr[0] and assign this
    # value to jumps[i]
  for i in range(1, n):
    jumps[i] = float('inf')
    for j in range(i):
      if (i <= j + arr[j]) and (jumps[j] != float('inf')):
        jumps[i] = min(jumps[i], jumps[j] + 1)
        break
  return jumps[n-1]

a = []
while True:
  s=input()
  if s =='*':
    break
  else:
    a.append(int(s))

print(f"\n{minJumps(a,len(a))} is the minimum jump")