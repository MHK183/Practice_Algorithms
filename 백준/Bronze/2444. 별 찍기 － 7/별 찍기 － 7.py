n = int(input())
output = ''

for i in range(-n+1, n):
    i = abs(i)
    output += ' '*i + '*'*(2*(n-i)-1) + '\n'
print(output)