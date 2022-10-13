def solution(my_string):
    
    alpha_mo = ['a', 'e', 'i', 'o', 'u']
    for i in alpha_mo:
        #예외 처리(replace는 예외가 발생해도 오류 x)
        if i in my_string:
            my_string = my_string.replace(i, '')
         
    return my_string