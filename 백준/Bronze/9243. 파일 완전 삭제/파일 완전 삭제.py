n = int(input())
before, after = input(), input()
result = True
if n % 2 == 1:
    for i in range(len(before)):
        if before[i] == after[i]:
            result = False
            break

    if result:
        print('Deletion succeeded')
    else:
        print('Deletion failed')
        
else:
    if before == after:
        print('Deletion succeeded')
    else:
        print('Deletion failed')