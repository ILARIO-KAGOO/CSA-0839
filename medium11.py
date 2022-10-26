max,min = map(int,input("Enter value (nth max, nth min): ").split())
l = list(map(int,input().split()))
l.sort()
print(f"{max}th maximum: {l[-max]} \n{min}th minimum: {l[min-1]}")