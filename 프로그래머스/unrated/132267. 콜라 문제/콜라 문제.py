def solution(a, b, n):
    answer = 0
    while n >= a: # 보유 중인 빈병이 a개 미만이면 콜라를 받을 수 없다
        add = n // a * b
        answer += add
        n = n % a + add 

    return answer