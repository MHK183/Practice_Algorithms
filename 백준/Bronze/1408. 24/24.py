a = list(map(int, input().split(':')))
b = list(map(int, input().split(':')))
time = []
x = a[0] * 3600 + a[1] * 60 + a[2]

if a[0] >= b[0]:
    y = b[0] * 3600 + b[1] * 60 + b[2] + 24*3600
else:
    y = b[0] * 3600 + b[1] * 60 + b[2]
    
result = y - x
h, m, s = 0, 0, 0
s += result
m += s // 60
h += m // 60

if h%24 < 10:
    if m%60 < 10:
        if s%60 < 10:
            print(f'0{h%24}:0{m%60}:0{s%60}')
        else:
            print(f'0{h%24}:0{m%60}:{s%60}')
    else:
        if s%60 < 10:
            print(f'0{h%24}:{m%60}:0{s%60}')
        else:
            print(f'0{h%24}:{m%60}:{s%60}')
else:
    if m%60 < 10:
        if s%60 < 10:
            print(f'{h%24}:0{m%60}:0{s%60}')
        else:
            print(f'{h%24}:0{m%60}:{s%60}')
    else:
        if s%60 < 10:
            print(f'{h%24}:{m%60}:0{s%60}')
        else:
            print(f'{h%24}:{m%60}:{s%60}')