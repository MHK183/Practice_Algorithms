T = int(input())

for _ in range(T):
    # 좌표값 저장
    x1, y1, x2, y2 = map(int, input().split())
    cnt = 0
    # 행성 정보 저장
    for _ in range(int(input())):
        Cx, Cy, r = map(int, input().split())
        
        check_duplicate = 0
        
        if ((Cx - x1)**2 + (Cy - y1)**2) < r**2:
            cnt += 1
            check_duplicate += 1
        if ((Cx - x2)**2 + (Cy - y2)**2) < r**2:
            cnt += 1
            check_duplicate += 1
            
        if check_duplicate == 2:
            cnt -= 2
            
    print(cnt)