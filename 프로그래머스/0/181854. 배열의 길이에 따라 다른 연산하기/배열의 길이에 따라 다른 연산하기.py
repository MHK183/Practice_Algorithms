def solution(arr, n):
    answer = [i for i in arr]
    length = len(arr)
    if length % 2 == 0:
        start = 1
    else:
        start = 0
    
    for i in range(start,length,2):
        answer[i] += n

    return answer