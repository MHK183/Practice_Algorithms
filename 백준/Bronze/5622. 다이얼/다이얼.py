call = input()
min_time = 0
for i in call:
    if i in 'ABC':
        min_time += 3
    elif i in 'DEF':
        min_time += 4
    elif i in 'GHI':
        min_time += 5
    elif i in 'JKL':
        min_time += 6
    elif i in 'MNO':
        min_time += 7
    elif i in 'PQRS':
        min_time += 8
    elif i in 'TUV':
        min_time += 9
    elif i in 'WXYZ':
        min_time += 10
print(min_time)

