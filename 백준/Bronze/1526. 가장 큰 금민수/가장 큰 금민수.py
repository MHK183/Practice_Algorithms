N = int(input())


for i in range(N, 3, -1):
    answer = True
    for j in str(i):
        
        if j != '4' and j != '7':
            answer = False
            break
            
    if answer:
        print(i)
        break
