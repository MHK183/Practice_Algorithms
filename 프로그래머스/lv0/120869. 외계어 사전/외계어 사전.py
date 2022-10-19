def solution(spell, dic):
    answer = 2
    spell = set(spell)
    for i in dic:
        if not spell - set(i):
            answer = 1
            break
    return answer