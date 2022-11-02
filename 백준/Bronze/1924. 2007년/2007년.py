month_days = [31,28,31,30,31,30,31,31,30,31,30]
weeks = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
Overall_day = 0
x, y = map(int, input().split())

for i in range(1, x):
    Overall_day += month_days[i-1]
Overall_day += y

print(weeks[(Overall_day-1) % 7])