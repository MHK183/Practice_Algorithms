def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    # 반복문 안에서 제거하므로 copy해서 사용
    reserve_cp = reserve.copy()
    lost_cp = lost.copy()
    
    # 여벌 옷을 가져온 학생이 도난 당했을 경우 제거
    for i in reserve:
        if i in lost:
            reserve_cp.remove(i)
            lost_cp.remove(i)
    lost = lost_cp.copy()
    
    for i in lost:
        if i-1 in reserve_cp:
            lost_cp.remove(i)
            reserve_cp.remove(i-1)
        elif i+1 in reserve_cp:
            lost_cp.remove(i)
            reserve_cp.remove(i+1)
        
    answer = n - len(lost_cp)
    return answer