def solution(lines):
    answer = 0
    a = []
    for line in lines:
        for i in range(min(line), max(line)):
            a.append(i)
    for i in range(min(a), max(a)+1):
        if a.count(i) >= 2:
            answer += 1
    
    return answer
