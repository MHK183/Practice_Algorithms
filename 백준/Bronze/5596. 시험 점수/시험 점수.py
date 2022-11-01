scores = []
for _ in range(2):
    scores.append(sum(list(map(int, input().split()))))
    
print(max(scores))