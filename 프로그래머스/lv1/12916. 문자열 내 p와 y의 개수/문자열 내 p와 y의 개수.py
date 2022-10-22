def solution(s):
    answer = True
    small_s = s.lower()
    if small_s.count('p') != small_s.count('y'):
        answer = False
    return answer