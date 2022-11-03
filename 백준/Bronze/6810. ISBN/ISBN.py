a = '9780921418'
for _ in range(3):
    a += input()
answer = 0   
for i in range(len(a)):
    if i % 2 == 0:
        answer += int(a[i]) * 1
    else:
        answer += int(a[i]) * 3

print(f'The 1-3-sum is {answer}')