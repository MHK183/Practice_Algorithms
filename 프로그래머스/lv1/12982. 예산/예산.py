def solution(d, budget):
    answer = 0
    money = 0
    d.sort()
    for i in d:
        money += i
        if money > budget:
            break
        else:
            answer += 1
    return answer