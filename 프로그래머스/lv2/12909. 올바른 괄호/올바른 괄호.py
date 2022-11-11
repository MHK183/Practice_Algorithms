def solution(s):
    answer = []
    for i in s:
        answer.append(i)
        if answer[-2:] == ['(',')']:
            for _ in range(2):
                answer.pop()

    if len(answer) == 0:
        return True
    else:
        return False
