a = int(input())
b = a
count = 0
while True:

    if b < 10:
        b = int(str(b) + str(b))
        count += 1
        if b == a:
            print(count)
            break
        else:
            continue
    else:
        b = int(str(b%10) + str((b//10 + b%10)%10))
        count += 1
        if b == a:
            print(count)
            break
        else:
            continue
        