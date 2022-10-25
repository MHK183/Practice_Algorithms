t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    a, b = x, y
    while b != 0:
        r = a % b
        (a, b) = (b, r)
    print((x // a) * (y // a) * a)
    