def solution(ingredient):
    a = []
    result = 0
    
    for i in ingredient:
        a.append(i)
        
        if a[-4:] == [1,2,3,1]:
            result +=1
            for _ in range(4):
                a.pop()
       
        

    return result