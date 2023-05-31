n, kim, lim = map(int, input().split())
count_round = 1

while True:
   
    
    if (kim % 2 == 1) and (kim + 1 == lim): # kim이 홀수이고 kim + 1 이 lim이면 이웃함
        print(count_round)
        break
    elif (kim % 2 == 0) and (kim - 1 == lim): # kim이 짝수이고 kim - 1 이 lim이면 이웃함
        print(count_round)
        break
    else:
        # 모두 아니면 다음 라운드로
        count_round += 1
        # n이 짝수면
        if n % 2 == 0:
            n //= 2
        else:
            n = n // 2 + 1
            
        kim = (kim + 1) // 2
        lim = (lim + 1) // 2