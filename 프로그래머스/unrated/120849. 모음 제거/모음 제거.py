def solution(my_string):
    
    alpha_mo = ['a', 'e', 'i', 'o', 'u']
    for i in alpha_mo:

        my_string = my_string.replace(i, '')
         
    return my_string