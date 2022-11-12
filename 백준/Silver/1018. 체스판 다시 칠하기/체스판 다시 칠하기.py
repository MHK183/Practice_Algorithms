n, m = map(int, input().split())
board = [input() for _ in range(n)]

chess_cases = []


for i in range(n-8 + 1):
    for j in range(m-8 + 1):
        case1, case2 = 0, 0

        for a in range(8):
            for b in range(8):
                # 왼쪽 맨위가 'W'로 칠해져 있을 때 경우 계산
                if a % 2 == 0: 
                    if b % 2 == 0 and board[a+i][b+j] == 'B':
                        case1 += 1
                    elif b % 2 == 1 and board[a+i][b+j] == 'W':
                        case1 += 1
                else:
                    if b % 2 == 0 and board[a+i][b+j] == 'W':
                        case1 += 1
                    elif b % 2 == 1 and board[a+i][b+j] == 'B':
                        case1 += 1
                # 왼쪽 맨위가 'B'로 칠해져 있을 때 경우 계산
                if a % 2 == 0: 
                    if b % 2 == 0 and board[a+i][b+j] == 'W':
                        case2 += 1
                    elif b % 2 == 1 and board[a+i][b+j] == 'B':
                        case2 += 1
                else:
                    if b % 2 == 0 and board[a+i][b+j] == 'B':
                        case2 += 1
                    elif b % 2 == 1 and board[a+i][b+j] == 'W':
                        case2 += 1

        chess_cases.append(min(case1, case2))
print(min(chess_cases))