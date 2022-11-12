n = int(input())
vote = input()
if vote.count('A') > vote.count('B'):
    print('A')
elif vote.count('A') == vote.count('B'):
    print('Tie')
else:
    print('B')