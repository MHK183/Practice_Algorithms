def solution(chicken):
    answer = 0
    (chicken // 10) + (chicken // 10) // 10
    while chicken >= 10:
        least = chicken % 10
        chicken = chicken // 10
        answer += chicken
        chicken += least
    return answer