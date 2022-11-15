import sys
input = sys.stdin.readline

# 에라토스 테네스체 알고리즘 start
a = [False, False] + [True for _ in range(2, 1000000 + 1)]

for i in range(2, int(1000000**(1/2)) + 1):

    if a[i] == True:
        j = 2
        while i * j <= 1000000:
            a[i*j] = False
            j += 1
# 에라토스 테네스체 알고리즘 end



while True:
    n = int(input())
    if n == 0:
        break
                
    # idx 가 숫자이고 a[idx] 가 True인 것이 소수라는 뜻
    # idx 가 소수이면서 n-idx 가 소수이면 정답
    # idx 가 작은 것부터 들어 가기에 차이가 가장 큰 값(b - a)은 처음 찾은 값이랑 같음
    for idx in range(3, len(a)):
        if a[idx] == True and a[n - idx] == True:
            print(f'{n} = {idx} + {n - idx}')
            break