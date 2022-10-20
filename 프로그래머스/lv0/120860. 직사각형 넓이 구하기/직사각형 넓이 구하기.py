def solution(dots):
    answer = 0
    sort_dots = sorted(dots, key = lambda x : [x[0], x[1]])
    dot1, dot2 = sort_dots[0], sort_dots[3]
    
    answer = (dot2[0] - dot1[0]) * (dot2[1] - dot1[1])
    return answer