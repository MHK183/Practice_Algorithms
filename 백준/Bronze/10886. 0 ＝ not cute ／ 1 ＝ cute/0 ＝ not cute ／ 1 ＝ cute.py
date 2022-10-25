n = int(input())
vote = []

for _ in range(n):
    vote.append(input())
    

if vote.count('1') > vote.count('0'):
    print('Junhee is cute!')
elif vote.count('1') < vote.count('0'):
    print('Junhee is not cute!')