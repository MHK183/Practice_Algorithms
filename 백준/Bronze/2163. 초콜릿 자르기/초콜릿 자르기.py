n, m  = map(int, input().split())
print(min(n, m)-1 + (max(n, m)-1)*min(n,m))