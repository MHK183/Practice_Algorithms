def solution(nums):
    l = len(nums) / 2
    kind = len(set(nums))
    if kind >= l:
        answer = l
    else:
        answer = kind
    return answer