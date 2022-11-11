def solution(X, Y):

    pair = ''
    for i in '0123456789':
        # 각 문자열(X, Y)의 숫자의 갯수 중
        # 작은 값이 공통된 숫자 갯수
        pair += i * min(X.count(i), Y.count(i)) 
                                                    

    # 짝궁이 존재하지 않을 때
    if len(pair) == 0:
        return "-1"
    # 문자열에 포함된 0의 개수와
    # 문자열의 길이가 같으면 0으로만 구성된 것이므로
    elif pair.count('0') == len(pair): 
        return "0"
    # 처음 문자열 더할 때 '0123456789' 대신
    # '9876543210'을 하면 sorted 할 필요 없음
    pair = ''.join(sorted(pair, reverse=True))
    return pair