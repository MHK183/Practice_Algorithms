answer = 0
for i in range(8):
    chess_board = input()
    answer += chess_board[i%2:8:2].count('F')
print(answer)