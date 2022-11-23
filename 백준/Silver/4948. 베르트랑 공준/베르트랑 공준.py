n = 123456*2
arr = [False, False] + [True for _ in range(n - 1)]

for i in range(2, int(n ** 1/2) + 1):
    if arr[i] == True:
        j = 2
        while i * j <= n:
            arr[i*j] = False
            j += 1

while True:
    k = int(input())
    
    if k == 0:
        break
    
    print(arr[k+1:k*2 + 1].count(True))