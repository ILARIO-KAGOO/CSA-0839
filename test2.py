str = input()
str = list(str)
vowels = ['a','e','i','o','u','A','E','I','O','U']
n = len(str)
str1 = ['*' if str[i] in vowels else str[i] for i in range(n)]
print("".join(str1),end="")