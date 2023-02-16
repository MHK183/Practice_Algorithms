N = input()
F = int(input())

A = int(N[:-2]) * 100

for _ in range(100):
    
    if A % F == 0:
        print(str(A)[-2:])
        break
    
    A += 1