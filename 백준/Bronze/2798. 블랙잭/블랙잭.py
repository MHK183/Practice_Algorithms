N, M = map(int, input().split())

card = sorted(list(map(int, input().split())))

answer = 0
for i in range(len(card) - 2):
    
    if i > 0 and card[i] == card[i-1]:
        continue
    left, right = i+1, len(card) - 1
    while left < right:
        sum_3 = card[i] + card[left] + card[right]
        if sum_3 > M:
            right -= 1
        elif sum_3 < M:
            left += 1
        else:
            answer = sum_3
            break
        if answer < sum_3 < M:
            answer = sum_3
    if answer == M:
        break
            
print(answer)