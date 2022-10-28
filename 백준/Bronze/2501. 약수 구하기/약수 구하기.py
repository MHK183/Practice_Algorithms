n, k = map(int, input().split())
n_list = [i for i in range(1, n+1) if n % i == 0]

if len(n_list) < k :
    print(0)
else:
    print(n_list[k-1])