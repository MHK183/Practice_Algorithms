def solution(n):
    fb = [0, 1]
    for i in range(n-1):
        fb.append(fb[i]+fb[i+1])
    return fb[n] % 1234567