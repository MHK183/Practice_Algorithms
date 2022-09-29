t = int(input())

for _ in range(t):
    r, s = input().split()
    r = int(r)
    new_s = ''
    
    for i in s:
        i *= r
        new_s += i
    print(new_s)