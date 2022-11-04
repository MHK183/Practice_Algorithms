for _ in range(int(input())):
    c = int(input())
    a = []
    for i in [25, 10, 5, 1]:
        a.append(c // i)
        c %= i
    a = list(map(str, a))
    print(' '.join(a))