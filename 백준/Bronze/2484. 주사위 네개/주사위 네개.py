from collections import Counter

money = []
for _ in range(int(input())):
    dice = list(map(int, input().split()))
    counter = Counter(dice)
    r_counter = {v:k for k,v in counter.items()}
    cnt = max(r_counter)
    if cnt == 4:
        money.append(50000 + r_counter[cnt]*5000)
    elif cnt == 3:
        money.append(10000 + r_counter[cnt]*1000)
    elif cnt == 2:
        if counter.most_common(n=2)[0][1] == counter.most_common(n=2)[1][1]:
            k = list(set(dice))
            money.append(2000 + k[0]*500 + k[1]*500)
        else:
            money.append(1000 + r_counter[cnt]*100)
    else:
        money.append(max(dice)*100)


print(max(money))