answer = 0
for i in range(1, 8 + 1):
    chess_board = input()
    if i % 2 == 1:
        answer += chess_board[0:8:2].count('F')
    else:
        answer += chess_board[1:8:2].count('F')
print(answer)