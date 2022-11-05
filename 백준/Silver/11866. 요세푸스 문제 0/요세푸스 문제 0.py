N, K = map(int, input().split())
arr = [i+1 for i in range(N)]
idx = 0
yose = []
while len(arr) != 0:
    idx = (idx + K - 1) % len(arr)
    yose.append(arr[idx])
    arr.remove(arr[idx])
    
yose = map(str, yose)
print(f"<{', '.join(yose)}>")