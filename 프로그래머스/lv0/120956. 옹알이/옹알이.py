def solution(babbling):
    # a, y, e, o, w, m
    answer = 0
    baby_word = ["aya", "ye", "woo", "ma"] 
    for i in babbling:
        idx = 0
        while len(i) >= 2:

            if i[:2] in baby_word or i[:3] in baby_word:
                i = i.replace(baby_word[idx], '', 1)
                # 할 수 있는 단어면 break
                if i == '':
                    answer += 1
                    break
                # 같은말 연속으로하면 break
                elif len(i) >= len(baby_word[idx]):
                    if i[:len(baby_word[idx])] == baby_word[idx]:
                        break
            else:
                break
            # 아무 단어도 포함되어 있지 않으면 break
                
            idx += 1
            
            if idx >= len(baby_word):
                idx = 0
        print(answer)        
    
    return answer