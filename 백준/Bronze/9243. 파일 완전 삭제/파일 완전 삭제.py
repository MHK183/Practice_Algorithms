n = int(input())
before, after = int(input(), 2), int(input(), 2)
result = bin(before + after)[2:]

if n % 2 == 1:
    if result.count('0') == 0:
        print('Deletion succeeded')
    else:
        print('Deletion failed')
else:
    if before == after:
        print('Deletion succeeded')
    else:
        print('Deletion failed')