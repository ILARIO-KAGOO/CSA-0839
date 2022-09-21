s = input("Enter first binary number: ")
d = input("Enter second binary number: ")
sumi = lambda a,b : bin(int(a, 2) + int(b, 2))

print(sumi(s,d)[2:])