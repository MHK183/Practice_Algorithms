n = int(input())
q1 = 0
q2 = 0
q3 = 0
q4 = 0
axis = 0
for _ in range(n):
    x, y = map(int, input().split())
    
    if x == 0 or y == 0:
        axis += 1
    elif x * y > 0:
        if x > 0:
            q1 += 1
        elif x < 0:
            q3 += 1
    elif x * y < 0:
        if x > 0:
            q4 += 1
        elif x < 0:
            q2 += 1
print('Q1: ' + str(q1))
print('Q2: ' + str(q2))
print('Q3: ' + str(q3))
print('Q4: ' + str(q4))
print('AXIS: ' + str(axis))