# a, b, c 는 각각 고정 비용, 가변비용, 노트북 비용
a, b, c = map(int, input().split())

# a + b * x = 비용
# c * x = 수익
# 수익 > 비용 : 손익 분기적

# 직선 cx 는 원점을 지나므로 bx + a 직선이 cx와 평행(b = c)하거나 기울기가 크면(b > c) 된다.
# 손익분기점이 없는 경우
if b >= c:
    print("-1")
else:
    # x는 노트북 개수, x 값이 한번에 정해져야함 : 시간초과 문제
    x = a / (c - b)
    # 나누기 때문에 정수형 변환
    print(int(x + 1))