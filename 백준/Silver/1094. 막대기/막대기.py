# 64를 기준으로 절반으로 잘라나가는 조합이니
# 붙힌 막대는 2의 제곱수로 이루어져있을 것
X = bin(int(input()))[2:]
print(X.count('1'))
