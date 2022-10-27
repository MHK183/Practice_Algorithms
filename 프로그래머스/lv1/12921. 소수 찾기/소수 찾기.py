def solution(n):
    answer = 0
    arr = [True for _ in range(n + 1)]

    for i in range(2, int(n**(1/2)) + 1):
        
        if arr[i] == True:
            j = 2
            while i * j <= n:
                arr[i*j] = False
                j += 1
    return arr.count(True) - 2