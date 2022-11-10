def solution(s):
    answer = ''
    for i in s.lower():
        if answer == '' or answer[-1] == ' ':
            answer += i.upper()
        else:
            answer += i

    return answer