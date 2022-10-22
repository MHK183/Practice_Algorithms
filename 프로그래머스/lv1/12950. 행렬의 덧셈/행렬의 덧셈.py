def solution(arr1, arr2):
    answer = []
    
    for x, y in zip(arr1, arr2):
        a = []
        for i in range(len(x)):
            a.append(x[i] + y[i])
        answer.append(a)
    return answer