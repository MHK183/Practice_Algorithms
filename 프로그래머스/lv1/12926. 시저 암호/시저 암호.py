def solution(s, n):
    answer = ''
    for j in s:
        if j.isupper():
            answer += chr(((ord(j) - ord('A') + n) % 26) + ord('A'))
        elif j.islower():
            answer += chr(((ord(j) - ord('a') + n) % 26) + ord('a'))
        else:
            answer += ' '
            
    return answer