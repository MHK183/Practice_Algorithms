t = int(input())

for _ in range(t):
    y_score = []
    k_score = []
    for _ in range(9):
        y, k = map(int, input().split())
        y_score.append(y)
        k_score.append(k)
    if sum(y_score) > sum(k_score):
        print("Yonsei")
    elif sum(y_score) < sum(k_score):
        print("Korea")
    else:
        print("draw")