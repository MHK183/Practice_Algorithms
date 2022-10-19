def solution(array, n):
    # 배열 array(정수)
    # 정수 n
    # array들어있는 정수 중 n과 가장 가까운 수
    abs_minus = [abs(i - n) for i in array]

    if abs_minus.count(min(abs_minus)) > 1:
        answer = n - min(abs_minus)
    else:
        answer = array[abs_minus.index(min(abs_minus))]
    return answer