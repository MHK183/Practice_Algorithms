scores = [int(input()) for _ in range(5)]

for idx, score in enumerate(scores):
    if score < 40:
        scores[idx] = 40
print(int(sum(scores) / len(scores)))