m = int(input())
d = int(input())

if 2 > m:
    print('Before')
elif m == 2:
    if 18 > d:
        print('Before')
    elif 18 == d:
        print('Special')
    else:
        print('After')
else:
    print('After')