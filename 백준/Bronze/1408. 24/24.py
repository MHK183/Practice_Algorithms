a = list(map(int, input().split(':')))
b = list(map(int, input().split(':')))
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
# f string :02d
print(f'{h%24:02d}:{m%60:02d}:{s%60:02d}')