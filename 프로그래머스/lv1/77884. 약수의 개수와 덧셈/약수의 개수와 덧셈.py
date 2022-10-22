def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        cnt = 0
        for j in range(1, i//2+1): # for문 반복수를 줄이기 위해 어림잡음
            if i % j == 0:
                cnt += 1
        cnt += 1 # 약수 중 가장 큰 수 더함
        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer