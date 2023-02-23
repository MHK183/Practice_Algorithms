 # N : 분(운동), m : 맥박 하한선(초기 맥박), M : 맥박 상한선,
 # T : 1분 동안 운동했을 때 증가하는 맥박, R : 1분 동안 휴식을한 후 감소하는 맥박
N, m, M, T, R = map(int, input().split())
# 현재 맥박
mac = m
# 필요한 시간
time = 0
while N > 0:
    
    # 운동을 못하는 조건
    if M - m < T:
        time = -1
        break

    # 운동 시작
    elif mac + T <= M:
        mac += T
        N -= 1
        time += 1
    # 휴식
    elif mac - R >= m:
        mac -= R
        time += 1
    # 휴식하는데 맥박이 하한선 이하로 떨어질 때
    elif mac - R < m:
        mac = m
        time += 1
    
    
print(time)
