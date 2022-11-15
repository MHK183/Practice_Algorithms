def solution(n):
    answer = 1
    
    for x in range(1, n // 2 + 1):
        n_sum = 0
        for i in range(x, n+1):
            n_sum += i
            if n_sum == n:
                answer += 1
                break
            elif n_sum > n:
                break
    return answer