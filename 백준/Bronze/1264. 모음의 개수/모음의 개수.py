mo = ['a','e','i','o','u','A','E','I','O','U']
while True:
    a = input()
    if a == '#':
        break
    cnt = 0
    for i in a:
        if i in mo:
            cnt += 1
    print(cnt)