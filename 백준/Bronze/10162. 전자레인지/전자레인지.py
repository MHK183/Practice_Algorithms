t = int(input())
a, b, c = 300, 60, 10
cnt_a, cnt_b, cnt_c = 0, 0, 0

if t % c != 0:
    print(-1)
else:
    if t >= a:
        cnt_a += t // a
        t %= a
    if t >= b:
        cnt_b += t // b
        t %= b
    if t >= c:
        cnt_c += t // c
    
    print(cnt_a, cnt_b, cnt_c)
    