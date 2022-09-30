x = int(input())
n = 1
while True:
    if 3 * (n ** 2) - 3 * n + 1 >= x:
        print(n)
        break
    n += 1