def combination(n, m):
    top = m
    bot = 1
    for _ in range(1, n):
        top *= m-1
        m -= 1
    for j in range(1, n+1):
        bot *= j
    return top // bot

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(combination(N, M))