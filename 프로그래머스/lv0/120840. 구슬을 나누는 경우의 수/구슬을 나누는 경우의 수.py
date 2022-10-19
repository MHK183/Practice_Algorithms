def solution(balls, share):
    # 콤비네이션 정의
    top, bottom = 1, 1
    for _ in range(share):
        top *= balls
        bottom *= share
        balls -= 1
        share -= 1

    return top / bottom