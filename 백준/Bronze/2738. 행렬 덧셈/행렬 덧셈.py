n, m = map(int, input().split())
a_list = []
b_list = []

for _ in range(n):
    a = list(map(int, input().split()))
    a_list.append(a)

for _ in range(n):
    b = list(map(int, input().split()))
    b_list.append(b)

for a, b in zip(a_list, b_list):
    for i, j in zip(a, b):
        print(i + j, end=' ')
    print()

