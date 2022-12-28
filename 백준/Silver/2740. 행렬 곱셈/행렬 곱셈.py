n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
    
m, k = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(m)]

C = []
for i in range(n):
    for x in range(k):
        c = 0
        for j in range(m):
            c += A[i][j] * B[j][x]
        print(c, end=' ')
    print()
    