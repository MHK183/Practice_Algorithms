def solution(answers):
    result = []
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    scores = [0, 0, 0]
    # 나머지를 이용해 반복
    for idx, answer in enumerate(answers):
        if s1[idx % len(s1)] == answer:
            scores[0] += 1
        if s2[idx % len(s2)] == answer:
            scores[1] += 1
        if s3[idx % len(s3)] == answer:
            scores[2] += 1
            
    for i in range(len(scores)):
        if max(scores) == scores[i]:
            result.append(i+1)
    return result