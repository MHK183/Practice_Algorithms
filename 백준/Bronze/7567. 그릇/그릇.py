a = input()
answer = 10
for idx, i in enumerate(a[1:]):
    if a[idx] == i:
        answer += 5
    else:
        answer += 10
print(answer)