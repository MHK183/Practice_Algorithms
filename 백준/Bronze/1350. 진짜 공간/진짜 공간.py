N = int(input())
file_size = list(map(int, input().split()))
cluster_size = int(input())
answer = 0

for i in file_size:
    if i == 0:
        continue
    elif i % cluster_size == 0:
        answer += (i // cluster_size) * cluster_size 
    elif i > cluster_size:
        answer += (i // cluster_size + 1) * cluster_size
    else:
        answer += cluster_size
print(answer)