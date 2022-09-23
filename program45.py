n = []

while True:
  s = input()
  if s == '*':
    break
  else:
    n.append(int(s))

print(f"index of the maximum element: {n.index(max(n))}")