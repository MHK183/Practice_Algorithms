answer = []
x = 0
for _ in range(4):
    a, b = map(int, input().split())
    x += b - a #현재 타고있는 사람 수
    
    answer.append(x)
print(max(answer))