def solution(num, total):
    answer = [i for i in range(total//num - num+1,total//num+1)]
    while sum(answer) != total:
        for i in range(num):
            answer[i] = answer[i]+1
        
    return answer