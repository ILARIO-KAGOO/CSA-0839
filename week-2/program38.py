def value(r):
  match(r):
    case 'I':
      return 1
    case 'V':
      return 5
    case 'X':
      return 10
    case 'L':
      return 50
    case 'C':
      return 100
    case 'D':
      return 500
    case 'M':
      return 1000
  return -1
def romantodecimal(str):
  res=0
  i=0
  while (i<len(str)):
    s1=value(str[i])
    if(i+1<len(str)):
      s2=value(str[i+1])
      if(s1>=s2):
        res=res+s1
        i=i+1
      else:
        res=res+s2-s1
        i=i+2
    else:
      res=res+s1
      i=i+1
  return res
message=str(input("s="))
try:
    n=romantodecimal(message)
    if n>3999:
        raise Exception()
    print(n)
except Exception:
    print("invalid input!try again!")