for _ in range(int(input())):
    k = int(input())
    n = int(input())
    apart = []
    first = [i for i in range(1, n+1)]
    apart.append(first)
    for i in range(k):
        a = []
        for j in range(1, n+1):
            a.append(sum(apart[i][:j]))
        apart.append(a)
    print(apart[k][n-1])