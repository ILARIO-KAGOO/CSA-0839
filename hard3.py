import string
str = input("Enter string: ")
str2 = ""
str1 = string.ascii_lowercase
for v in str:
	c = str.count(v)
	s = str1.find(v)
	str2 += str1[s+c]
print(str2)