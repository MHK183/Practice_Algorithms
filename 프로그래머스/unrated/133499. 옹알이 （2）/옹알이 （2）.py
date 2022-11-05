def solution(babbling):
    c = 0
    for b in babbling:
        for w in [ "aya", "ye", "woo", "ma" ]:
            if w * 2 not in b:  # 연속해서 같은 발음이 있는지 먼저 분류
                b = b.replace(w, ' ')
        if len(b.rstrip()) == 0:
            c += 1
    return c