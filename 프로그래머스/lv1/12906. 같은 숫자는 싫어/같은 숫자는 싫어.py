def solution(arr):
    answer = [arr[0]]
    
    if len(arr) >= 2:
        for idx, i in enumerate(arr[1:]):
            answer.append(i)
            if i == arr[idx]:
                answer.pop()
        return answer        
    else:
        return answer