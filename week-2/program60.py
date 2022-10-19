import numpy as np
l = []
while True:
  s = input()
  if s == '*':
    break
  else:
    l.append(int(s))
lc = np.lcm.reduce(l)
gc = np.gcd.reduce(l)

print(f"LCM = {lc} \nGCD = {gc}")