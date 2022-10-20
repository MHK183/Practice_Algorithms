def solution(num, total):
    answer = [i for i in range(total//num - num,total//num)]
    while sum(answer) != total:
        for i in range(num):
            answer[i] = answer[i]+1
        
    return answer