n = int(input("Enter choice(pow,add,sub,mul,div): "))
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

match(n):
  case 1:
    print(f"Pow({a},{b}): {a**b}")
  case 2:
    print(f"Add({a},{b}): {a+b}")
  case 3:
    print(f"Sub({a},{b}): {a-b}")
  case 4:
    print(f"Mul({a},{b}): {a*b}")
  case 5:
    print(f"Div({a},{b}): {a/b}")
  case other:
    print("Invalid choice(only from 1-5)")
  