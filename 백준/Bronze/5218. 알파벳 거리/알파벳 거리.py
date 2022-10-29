for _ in range(int(input())):
    x, y = input().split()
    print('Distances: ',end='')
    for a, b in zip(x, y):
        if a > b:
            d = ord(b)+26 - ord(a)
        else:
            d = ord(b) - ord(a)
        print(d, end=' ')
    print()