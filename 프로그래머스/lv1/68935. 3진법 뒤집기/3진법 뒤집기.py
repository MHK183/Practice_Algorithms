def solution(n):
    n_3 = ''
    while n >= 1:
        n_3 += f'{n % 3}'
        n //= 3
    
    return int(n_3, 3) 