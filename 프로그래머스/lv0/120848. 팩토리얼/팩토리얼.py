def solution(n):
    i = 1
    factorial = 1
    while True:
        factorial *= i
        if n < factorial:
            return i - 1
        elif n == factorial:
            return i
        i += 1
        
        
        
