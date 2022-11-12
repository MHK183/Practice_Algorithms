t = int(input())

for i in range(t):
    output = ''
    for _ in range(1, t-i):
        output += ' '
    output += ('*' * (i+1))
    print(output)