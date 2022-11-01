def solution(dartResult):
    idx = 0
    scores = []
    for i in range(3): # 조건 1
        
        # 조건 2 (10과 같은 두자릿수 일경우)
        if dartResult[idx:idx+2].isdigit():
            score = int(dartResult[idx:idx+2])
            idx += 2
        elif dartResult[idx].isdigit():
            score = int(dartResult[idx])
            idx += 1

        # 조건 3 보너스 판별
        if dartResult[idx] == 'S':
            score **= 1
        elif dartResult[idx] == 'D':
            score **= 2
        elif dartResult[idx] == 'T':
            score **= 3
            
        scores.append(score)
        idx += 1
        # 마지막 게임에서 옵션이 안붙었을 경우 예외 처리
        if idx >= len(dartResult):
            break

        # 옵션 판별
        if dartResult[idx].isdigit():
            continue
        elif dartResult[idx] == '*':
            if i == 0:            # 조건 5 해당
                scores[i] *= 2
            else:  # 조건 4
                scores[i-1] *= 2
                scores[i] *= 2
        elif dartResult[idx] == '#':  # 조건 4
            scores[i] *= -1
        
        idx += 1

        
    return sum(scores)            
        