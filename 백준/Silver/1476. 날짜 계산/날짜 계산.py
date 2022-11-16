junkyu = list(map(int, input().split()))
we = [0, 0, 0]
esm_range = [15, 28, 19]
answer = 0
while True:
    if junkyu == we:
        print(answer)
        break
    for i, j in zip(range(len(we)), esm_range):
        we[i] += 1
        if we[i] > j:
            we[i] %= j
    
    answer += 1