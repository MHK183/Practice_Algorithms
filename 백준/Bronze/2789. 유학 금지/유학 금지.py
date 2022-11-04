a = 'CAMBRIDGE'

s = input()
answer = ''
for i in s:
    if i not in a:
        answer += i
print(answer)