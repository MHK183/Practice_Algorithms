n = int(input())
output = ''
for i in range(n):
    for _ in range(n - i):
        output += '*'
    output += '\n'
print(output[:-1])