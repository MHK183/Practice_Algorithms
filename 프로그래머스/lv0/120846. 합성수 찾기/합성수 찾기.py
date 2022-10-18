def solution(n):
    answer = 0
    for i in range(1, n+1):
        numbers = []
        for j in range(1, i+1):
            if i % j == 0:
                numbers.append(j)
        if len(numbers) >= 3:
            answer += 1  
    return answer