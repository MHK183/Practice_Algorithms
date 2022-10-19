def solution(spell, dic):
    answer = 2
    for i in dic:
        if len(i) >= len(spell):
            for j in spell:
                i = i.replace(j, '', 1)
            if len(i) == 0:
                answer = 1
    return answer