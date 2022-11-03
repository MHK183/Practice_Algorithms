a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_score = 0
b_score = 0
for i in range(len(a)):
    if a[i] > b[i]:
        a_score += 1
    elif b[i] > a[i]:
        b_score += 1
if a_score > b_score:
    print('A')
elif b_score > a_score:
    print('B')
else:
    print('D')