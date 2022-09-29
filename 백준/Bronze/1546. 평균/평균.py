a = int(input())
b = list(map(int, input().split()))
c = []
m = max(b)

for i in b:
    new_score = i / m * 100
    c.append(new_score)

print(sum(c) / a)