X = int(input())
# 길이가 64인 막대를 가지고 있다
stick_length = [64]

# 가지고있는 막대의 합이 X보다 크다면 아래의 과정을 반복
# 만약 가지고있는 막대의 합이 X보다 작은 상태로 나오면 문제가 되지 않을까?
while sum(stick_length) > X:
    
    # 1-1. 길이가 가장 짧은 것을 절반으로 자른다
    shortest = min(stick_length) // 2
    # 1-1. 쉽게 비교하기 위해 제거
    stick_length.remove(min(stick_length))
    
    # 1-2. 만약, 위에서 자른 막대의 절반(shortest) 중 하나를 버리고 
    #      남아있는 막대의 길이의 합(shortest + sum(stick_length))
    #      이 같으면 자른 막대의 절반 중 하나를 버린다.
    #      따라서 한번만 append 해줌
    if shortest + sum(stick_length) >= X:
        stick_length.append(shortest)
    #      아니라면 2 번 append
    else:
        stick_length.append(shortest)
        stick_length.append(shortest)

print(len(stick_length))