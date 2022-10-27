def solution(s):
    arr = [int(i) for i in s.split()]
    return f'{min(arr)} {max(arr)}'