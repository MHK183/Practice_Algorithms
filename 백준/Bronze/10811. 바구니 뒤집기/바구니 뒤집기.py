N, M = map(int, input().split())
baskets = [i+1 for i in range(N)]

for _ in range(M):
    i, j = map(int, input().split())
    baskets = baskets[:i-1] + list(reversed(baskets[i-1:j])) + baskets[j:]
print(" ".join(map(str, baskets)))