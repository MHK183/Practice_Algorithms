n = int(input())
results = input().split()
score = 0
k = 0
for result in results:
    if result == '1':
        k += 1
        score += k
    elif result == '0':
        k = 0
print(score)
    