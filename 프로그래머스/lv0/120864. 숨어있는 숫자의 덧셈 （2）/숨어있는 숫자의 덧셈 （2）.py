def solution(my_string):
    answer = 0
    idx = 0
    while idx < len(my_string):
        my = ''
        i = my_string[idx]
        if i.isdigit():
            my += i
            for j in my_string[idx+1:]:

                if not j.isdigit():
                    break
                elif j.isdigit():
                    idx += 1
                    my += j

            answer += int(my)
        idx += 1    

    return answer