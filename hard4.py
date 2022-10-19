month = input("Input the month (e.g. Jan, Feb etc.): ")
day = int(input("Input the day: "))
if month in ('Jan', 'Feb', 'Mar'):
	season = 'winter'
elif month in ('Apr', 'May', 'June'):
	season = 'spring'
elif month in ('July', 'Aug', 'Sep'):
	season = 'summer'
else:
	season = 'autumn'
if (month == 'Mar') and (day > 19):
	season = 'spring'
elif (month == 'June') and (day > 20):
	season = 'summer'
elif (month == 'Sep') and (day > 21):
	season = 'autumn'
elif (month == 'Dec') and (day > 20):
	season = 'winter'
print("Season is",season)