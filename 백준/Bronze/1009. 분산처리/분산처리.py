import sys
input = sys.stdin.readline


for i in range(int(input())):
    a, b = map(int, input().split())
    result = 1
    for j in range(b):
        result *= a
        result = int(str(result)[-1])
        
    answer = str(result)[-1]
    
    if answer == "0":
        print("10")
    else:
        print(answer)