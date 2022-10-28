n = int(input())
array = list(map(int, input().split()))
cnt = 0

for i in array:
    cnt += 1
    if i == 1:
        cnt -= 1
    
    for j in range(2, i):
        
        if i % j == 0:
            cnt -= 1
            break
print(cnt)
            