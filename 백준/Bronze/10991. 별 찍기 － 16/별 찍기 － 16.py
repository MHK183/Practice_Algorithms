n = int(input())
output = ''
for i in range(n):
    output += ' '*(n-1 - i)
    output += ('*' + ' ') * (i+1)
    output += '\n'
print(output)