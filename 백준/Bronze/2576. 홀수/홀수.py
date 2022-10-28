oddnums = []
for _ in range(7):
    n = int(input())
    if n % 2 != 0:
        oddnums.append(n)

if len(oddnums) == 0:
    print(-1)
else:
    print(sum(oddnums))
    print(min(oddnums))