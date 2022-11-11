def solution(survey, choices):
    answer = ''
    mbti_dic = {'R':0, 'T':0,
               'C':0, 'F':0,
               'J':0, 'M':0,
               'A':0, 'N':0}
    a = [0,3,2,1,4,5,6,7]
    for i, choice in zip(survey, choices):
        if choice > 4:
            mbti_dic[i[1]] += a[choice] % 4
        elif choice < 4:
            mbti_dic[i[0]] += a[choice] % 4
    
    for j in ["RT", "CF", "JM", "AN"]:
        if mbti_dic[j[0]] >= mbti_dic[j[1]]: # RT, CF, JM, AN 전부 사전 순이기 때문
            answer += j[0]
        else:
            answer += j[1]
            

    return answer