def solution(s):
    s_list = s.split()
    a = []
    for i in s_list:
        if i == 'Z':
            # Z가 나오면 가장 최근 값 제거
            a.pop()
        else:
            a.append(int(i))
    return sum(a)
            