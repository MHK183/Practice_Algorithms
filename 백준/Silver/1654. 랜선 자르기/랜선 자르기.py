K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]
total_length = sum(cables)

start = 1
end = total_length // N

while start <= end:
    middle = (start+end) // 2
    count = 0
    for cable in cables:
        count += cable // middle

    if count >= N:
        start = middle + 1
    else:
        end = middle - 1
print(end)

