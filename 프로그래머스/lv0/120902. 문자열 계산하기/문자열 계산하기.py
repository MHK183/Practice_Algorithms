def solution(my_string):
    num_oper = my_string.split()
    answer = int(num_oper[0])
    for i in range(len(num_oper[1::2])):        
        
        if num_oper[2*i+1] == '+':
            answer += int(num_oper[2*(i+1)])
            
        elif num_oper[2*i+1] == '-':
            answer -= int(num_oper[2*(i+1)])

    
    return answer