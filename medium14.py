s = input("Enter string: ")
if "-" in s : s=s.replace("-","")
print(f"mirror image: {s[::-1]}")