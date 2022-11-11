def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()
    # 2단계
    for i in new_id:
        if i.isalnum() or i in '-_.':
            answer += i
    # 3단계
    while answer.count('..') != 0:
        answer = answer.replace('..', '.')
        
    # 4단계
    if answer[:1] == '.':
        answer = answer[1:]
    if answer[-1:] == '.':
        answer = answer[:-1]
    
    # 5단계
    if answer == '':
        answer += 'a'
    
    # 6단계
    answer = answer[:15]
    if answer[-1:] == '.':
        answer = answer[:-1]
    # 7단계
    while len(answer) <= 2:
        answer += answer[-1]
    
    
    return answer