year = int(input("Enter a year: "))

if year%400==0:
  if year%100==0: 
    print(f"{year} is a leap year.")
    
  else:
    if year%4==0:
      print(f"{year} is a leap year.")
    else:
      print(f"{year} is not a leap year.")
      s = year - int(year%4)
      print(f"Leap year: {s}")
else:
   print(f"{year} is not a leap year.")
   s = year - int(year%4)
   print(f"Leap year: {s}")
