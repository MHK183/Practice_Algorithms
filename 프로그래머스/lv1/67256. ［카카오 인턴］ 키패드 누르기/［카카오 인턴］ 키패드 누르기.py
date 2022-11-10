def solution(numbers, hand):
    answer = ''
    key = [(0,1),(3,0),(3,1),(3,2),(2,0),(2,1),(2,2),(1,0),(1,1),(1,2)]
    right_num = [3,6,9]
    left_num = [1,4,7]
    mid_num = [0,2,5,8]
    
    left_loc = (0,0)
    right_loc = (0,2)
    
    for number in numbers:
    
        if number in mid_num:
            left_distance = abs(key[number][0] - left_loc[0]) + abs(key[number][1] - left_loc[1])
            right_distance = abs(key[number][0] - right_loc[0]) + abs(key[number][1] - right_loc[1])
            
            if  left_distance < right_distance:
                answer += 'L'
                left_loc = key[number]
            elif left_distance > right_distance:
                answer += 'R'
                right_loc = key[number]
            else:
                if hand == 'right':
                    answer += 'R'
                    right_loc = key[number]
                elif hand == 'left':
                    answer += 'L'
                    left_loc = key[number]
                
        elif number in right_num:
            answer += 'R'
            right_loc = key[number]
        elif number in left_num:
            answer += 'L'
            left_loc = key[number]
    
    
    
    return answer