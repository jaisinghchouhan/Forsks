days=input("enter the days").split(",")
t_days=('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
for item in t_days:
    if item not in days:
        days.append(item)
ndays=tuple(days)
print(ndays)    