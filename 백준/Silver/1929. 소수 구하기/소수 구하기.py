
m, n = map(int, input().split())

arr = [False, False] + [True for _ in range(2, n + 1)]

for i in range(2, int(n**(1/2)) + 1):

    if arr[i] == True:
        j = 2
        while i * j <= n:
            arr[i*j] = False
            j += 1
for i in range(m, len(arr)):
    if arr[i] == True:
        print(i)