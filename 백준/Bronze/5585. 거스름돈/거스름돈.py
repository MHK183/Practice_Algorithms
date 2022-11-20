n = 1000 - int(input())

cnt = 0
exchange = [500, 100, 50, 10, 5, 1]

for i in exchange:
    cnt += n // i
    n %= i
print(cnt)