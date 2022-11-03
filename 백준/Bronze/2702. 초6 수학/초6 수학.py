for _ in range(int(input())):
    a, b = map(int, input().split())
    s = a * b
    while b != 0:
        r = a % b
        a, b = b, r
    print(s // a, a)