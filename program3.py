def numSquareSum(n):
    squareSum = 0;
    while(n):
        squareSum += (n % 10) * (n % 10);
        n = int(n / 10);
    return squareSum;
    
def isHappyNumber(n):
    st=set()
    while (1):
        n = numSquareSum(n)
        if (n == 1):
            return True
        if n not in st:
            return False
        st.insert(n)

s = int(input("Enter number: "))
if isHappyNumber(s):
  print(f"{s} is a happy number")
else:
  print(f"{s} is not a happy number")