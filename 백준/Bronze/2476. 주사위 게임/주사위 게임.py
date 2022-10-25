n = int(input())
answer = []
for _ in range(n):
    dice = list(map(int, input().split()))
    if len(set(dice)) == 1:
        answer.append(10000+dice[0]*1000)
    elif len(set(dice)) == 2:
        for i in dice:
            if dice.count(i) == 2:
                answer.append(1000+i*100)
                break
    else:
        answer.append(max(dice)*100)
print(max(answer))