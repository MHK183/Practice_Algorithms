def solution(X, Y):

    pair = ''
    for i in '0123456789':
        if i in X and i in Y:
            # 각 문자열(X, Y)의 숫자의 갯수 중
            # 작은 값이 공통된 숫자 갯수
            pair += i * min(X.count(i), Y.count(i)) 
                                                    

    # 짝궁이 존재하지 않을 때
    if len(pair) == 0:
        return "-1"
    elif pair.count('0') == len(pair): # 0의 개수와 길이가 같으면 0으로만 구성된 것이므로
        return "0"
    
    pair = ''.join(sorted(pair, reverse=True))
    return pair