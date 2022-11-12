def solution(s):
    bin_cnt = 0
    zero_cnt = 0
    
    while len(s) != 1:
        
        l = s.count('1')
        
        zero_cnt += len(s) - l
        s = s.replace('0','')
        s = bin(l)[2:]
        bin_cnt += 1
    return [bin_cnt, zero_cnt]