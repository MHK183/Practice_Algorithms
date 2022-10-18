def solution(num_list, n):
    answer = []
    
    for i in range(0, len(num_list), n):
        a_list = []
        for j in range(i, n+i):
            a_list.append(num_list[j])
        answer.append(a_list)

    return answer