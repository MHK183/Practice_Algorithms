def solution(denum1, num1, denum2, num2):
    answer = [denum1 * num2 + denum2 * num1, num1 * num2]
    # 분모 분자의 최대 공약수 k 를 구함
    for i in range(1, min(answer) + 1):
        if answer[0] % i == 0 and answer[1] % i == 0:
            k = i
    # 최대 공약수로 약분한다 ( // 로 해준 이유는 출력값이 int형으로 나와야함)
    # 어차피 공약수로 약분하기에 소수점아래에 값이 나오진 않음 
    answer = [ answer[0] // k, answer[1] // k]    
    return answer