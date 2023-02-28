y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

day_1 = d1
day_2 = d2


# 그 해의 월을 일수로 변환
def month_to_day(y, m):
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0
    
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        for i in range(1, m):
            day += month2[i-1]
    else:
        for i in range(1, m):
            day += month[i-1]
    
    return day

day_1 += month_to_day(y1, m1)
day_2 += month_to_day(y2, m2)


# 년도를 일수로 계산
y1 = y1 - 1
y2 = y2 - 1
day_1 += y1 * 365 + (y1 // 4 - y1 // 100 + y1 // 400)
day_2 += y2 * 365 + (y2 // 4 - y2 // 100 + y2 // 400)

answer = day_2 - day_1


if (y2 - y1 > 1000) or \
    (y2 - y1 == 1000 and m2 > m1) or \
    (y2 - y1 == 1000 and m2 == m1 and d2 >= d1):
    print('gg')
else:
    print(f'D-{answer}')