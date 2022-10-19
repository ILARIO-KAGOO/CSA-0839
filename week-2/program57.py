import statistics as st
l = []
while True:
  s = input()
  if s == '*':
    break
  else:
    l.append(int(s))

print(f"Mean = {st.mean(l)}")
print(f"Median = {st.median(l)}")
print(f"Mode = {st.mode(l)}")