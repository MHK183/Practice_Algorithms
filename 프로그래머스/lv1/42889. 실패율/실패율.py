def solution(N, stages):
    # 스테이지 1을 셀 때
    # 1번 스테이지 갯수 / 1번 스테이지 포함 전체 갯수
    # 스테이지 2를 셀 때
    # 2번 스테이지 갯수 / 2번 스테이지 포함 전체 갯수
    # 스테이지 n을 셀 때
    # n번 스테이지 갯수 / n번 스테이지 포함 전체 갯수
    # 실패율이 높은 스테이지부터 내림차순으로 출력
    # 같은 경우 작은 번호의 스테이지가 앞으로
    # 스테이지에 도달한 유저가 없는 경우 0
    fail = []
    stages.sort()

    for i in range(1, N+1):
        if i not in stages:
            fail.append((i, 0))
            continue
            
        top = stages.count(i)
        bot = len(stages[stages.index(i):])

        fail.append((i,top/bot))
        
    fail.sort(key=lambda x : x[1], reverse = True)
    answer = [i for i, _ in fail]
    return answer