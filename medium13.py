from statistics import mean
l = [[],[]]
print("Enter -1 to exit: ")
while True:
  s = input()
  if s == "-1": break
  if int(s) < -1:
    l[0].append(int(s))
  elif int(s) >= 0:
    l[1].append(int(s))
print(f"Average of postive: {mean(l[0])} \nAverage of negative number: {round(mean(l[1]),2)}")
