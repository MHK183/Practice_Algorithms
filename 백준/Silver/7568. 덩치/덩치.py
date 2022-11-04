a = [list(map(int, input().split())) for _ in range(int(input()))]

for i in range(len(a)):
    rank = 1
    for j in range(len(a)):
        if i == j:
            continue
        elif a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            rank += 1
    print(rank, end=' ')