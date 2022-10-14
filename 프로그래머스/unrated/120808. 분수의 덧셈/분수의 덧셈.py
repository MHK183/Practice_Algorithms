def solution(denum1, num1, denum2, num2):
    answer = [denum1 * num2 + denum2 * num1, num1 * num2]
    for i in range(1, min(answer) + 1):
        if answer[0] % i == 0 and answer[1] % i == 0:
            k = i
    answer = [ answer[0] // k, answer[1] // k]    
    return answer