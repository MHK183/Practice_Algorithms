def solution(lottos, win_nums):

    k = [6, 6, 5, 4, 3, 2, 1]
    
    a = lottos.count(0)
    cnt = 0
    for win_num in win_nums:
        if win_num in lottos:
            cnt += 1
    answer = [k[a+cnt], k[cnt]]
    return answer