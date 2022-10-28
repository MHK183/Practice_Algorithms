n = int(input())
output = ''

for i in range(1, n+1):
    output += ' '*(n - i) + '*'*(2*i-1) + '\n'
for j in range(n-1, 0, -1):
    output += ' '*(n - j) + '*'*(2*j-1) + '\n'
    
print(output)