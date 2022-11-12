def solution(s):
    bin_cnt = 0
    zero_cnt = 0
    
    while len(s) != 1:
        string = ''    
        for i in s:
            if i == '1':
                string += i
            else:
                zero_cnt += 1
        
        l = len(string)
        s = bin(l)[2:]
        bin_cnt += 1
    return [bin_cnt, zero_cnt]