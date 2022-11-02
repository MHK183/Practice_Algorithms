month_days = [31,28,31,30,31,30,31,31,30,31,30]
weeks = ['Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday']
Overall_day = 0
y, x = map(int, input().split())

for i in range(1, x):
    Overall_day += month_days[i-1]
Overall_day += y

print(weeks[(Overall_day-1) % 7])