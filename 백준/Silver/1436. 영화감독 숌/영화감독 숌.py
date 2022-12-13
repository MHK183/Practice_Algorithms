n = int(input())
arr = []
i = 0
while True:
    i += 1
    
    if str(i).count('666') >= 1:
        arr.append(i)
        if len(arr) == n + 1:
            print(arr[n-1])
            break
