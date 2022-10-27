def solution(answers):
    answer = []
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    s1_score, s2_score, s3_score = 0, 0, 0

    l = len(answers)
    for i in range(l):
        k = i
        i %= len(s1)
        if s1[i] == answers[k]:
            s1_score += 1
            
        i = k
        
        i %= len(s2)
        if s2[i] == answers[k]:
            s2_score += 1
            
        i = k
        
        i %= len(s3)
        if s3[i] == answers[k]:
            s3_score += 1
            
    scores = [s1_score, s2_score, s3_score]

    for i in range(len(scores)):
        if max(scores) == scores[i]:
            answer.append(i+1)
    return answer