def solution(numbers):
    answer = 0
    a = []
    for k, i in enumerate(numbers):

        if k == len(numbers) - 1:

            break
        else:    
            for j in numbers[k+1:]:
                a.append(i*j)
        
    answer = max(a)
    return answer