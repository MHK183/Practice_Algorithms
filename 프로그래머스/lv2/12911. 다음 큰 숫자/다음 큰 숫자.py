def solution(n):
    k = (bin(n)[2:]).count('1')
    while True:
        n += 1
        
        if (bin(n)[2:]).count('1') == k:
            answer = n
            break
        
    return answer