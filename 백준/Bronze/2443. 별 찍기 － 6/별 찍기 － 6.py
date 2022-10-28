n = int(input())
output = ''

for i in range(n, 0, -1):
    output += ' '*(n-i) + '*'*(2*i-1) + '\n'
    
print(output)