str1 = inpu
str2 = input("Enter second string: ")

str1_i = max(str1,str2)
str2_i = min(str1,str2)

for i in str1_i:
  for j in str2_i:
    if i == j:
      str1_i=str1_i.replace(i,"")
      str2_i=str2_i.replace(i,"")

str = str1_i+str2_i
print(str)
