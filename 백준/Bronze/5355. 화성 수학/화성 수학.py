t = int(input())

for _ in range(t):
    a = input().split()
    k = float(a[0])
    for i in a[1:]:
        if i == '@':
            k *= 3
        elif i == '%':
            k += 5
        elif i == '#':
            k -= 7

    print('{:.2f}'.format(k))
        
        