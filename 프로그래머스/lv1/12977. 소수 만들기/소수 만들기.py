def solution(nums):
    answer = 0
    l = len(nums)
    for i in range(l-2):
        for j in range(i+1, l-1):
            for k in range(j+1, l):
                e = nums[i] + nums[j] + nums[k]
                answer += 1
                for x in range(2, int(e**(1/2))+1):
                    if e % x == 0:
                        answer -= 1
                        break
    return answer