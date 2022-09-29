h , m = map(int, input().split())
c = int(input())

if c >= 60:
    if m + c%60 >= 60:
        print((h+c//60+1)%24, (m+c%60)%60)
    else:
        print((h+c//60)%24, m+c%60)
else:
    if m + c >= 60:
        print((h+1)%24, (m+c)%60)
    else:
        print(h%24,m+c)