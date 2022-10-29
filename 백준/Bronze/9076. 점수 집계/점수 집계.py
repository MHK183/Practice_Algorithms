for _ in range(int(input())):
    scores = sorted(list(map(int, input().split())))
    scores = scores[1:-1]
    if scores[-1] - scores[0] >= 4:
        print('KIN')
    else:
        print(sum(scores))
    