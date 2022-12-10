# 9, 90, 900, 9000, 90000, 900000, 9000000, 90000000

n = int(input())
k = 1 
i = 1 # 자릿수
count = 0
while True:
    
    # 자리수가 같아지면 더하고 종료
    if len(str(n)) == len(str(k)):
        count += (n - k + 1) * i
        break
    # 1의 자리수 9개, 10의 자리수 90개
    count += k * 9 * i
    i += 1
    k *= 10
    

print(count)