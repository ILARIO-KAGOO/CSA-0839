upper,lower,number = 0,0,0
while True:
  s = input()
  if s == "*": break
  elif s.isalnum():
    if s.isupper(): upper+=1
    elif s.islower(): lower+=1
    elif s.isnumeric(): number+=1

print(f"total count of lowercase: {lower} \ntotal count of uppercase: {upper} \ntotal count of number: {number}")