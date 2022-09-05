inputList = list(map(int,input().split()))
dict = {}

for i in inputList:
  dict[i] = []

i=0
for j in inputList:
  dict[j].append(i)
  i+=1

res_dict={}

for key,val in dict.items():
  if len(val) >= 2:
    res_dict[key]=val

print(res_dict,end="")