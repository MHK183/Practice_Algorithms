while True:
    n, s = map(int, input().split())
    if n == 0 and s == 0:
        break
    if n > s:
        print("Yes")
    else:
        print("No")
