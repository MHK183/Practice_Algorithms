def solution(a, b):
    # 작은 값의 약수를 기준으로 최대 공약수
    nums = [min(a, b), max(a, b)]
    yaksu = [i for i in range(1, nums[0] + 1) if nums[0] % i == 0]
    # k가 최대 공약수가 됨
    for i in yaksu:
        if nums[1] % i == 0:
            k = i
    # 분모를 k로 나눠 약분 한 값의 소인수를 구함
    new_b = b / k
    idx = 2
    new_b_so = []
    while new_b > 1:

        if new_b % idx == 0:
            new_b /= idx
            new_b_so.append(idx)
            continue
        idx += 1
    # 중복제거 (소인수 구하기)
    answer = list(set(new_b_so))
    if 2 in answer:
        answer.remove(2)
    if 5 in answer:
        answer.remove(5)
    
    if len(answer) == 0:
        return 1
    else:
        return 2