scores = []

for _ in range(8):
    score = int(input())
    scores.append(score)

sort_scores = sorted(scores.copy())
sum_score = sum(sort_scores[3:])
print(sum_score)
      
for i in range(8):
    if sort_scores[3] <= scores[i]:
        print(i+1, end=' ')