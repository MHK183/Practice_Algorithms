n = int(input())
result = []
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            result.append((x+i, y+j))

result = list(set(result)) # 좌표 중복 제거
    
print(len(result)) # 좌표 하나당 넓이 1로 생각