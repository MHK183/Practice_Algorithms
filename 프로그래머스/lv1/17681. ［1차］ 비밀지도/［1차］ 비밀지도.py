def solution(n, arr1, arr2):
    # arr1, arr2 1행 씩 꺼내서 2진수로 변환 후
    # or 연산해서 1인 값을 # 0인 값을 ' '으로
    answer = []
    for i, j in zip(arr1, arr2):
        a = bin(i | j)[2:]
        if len(a) != n:
            a = '0'*(n-len(a)) + a
        a = a.replace('1', '#')
        a = a.replace('0', ' ')
        answer.append(a)
            
    return answer