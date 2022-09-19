from tkinter import N


list =[]
n =""
print("Enter marks (enter * to quit):",end="\n")
while True:
  n = input()
  if n=="*":
    break
  else:
    list.append(int(n))

j=1
print("\n")
for i in list:
  if i>=90:
    print(f"{j} student got A grade.")
  elif i>=70:
    print(f"{j} student got B grade.")
  elif i>=50:
    print(f"{j} student got C grade.")
  else:
    print(f"{j} student as failed.")
  j+=1

print(f"\ntotal marks in class = {sum(list)}")
print(f"Avg marks in class = {sum(list)/len(list)}")