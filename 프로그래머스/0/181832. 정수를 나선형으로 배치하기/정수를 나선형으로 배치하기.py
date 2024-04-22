def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    row = 0
    col = 0
    num = 1
    direction = 'right'
    for _ in range(n**2):
        is_out_of_index = False
        answer[row][col] = num
        # 움직이는 방향에 따라 이동
        if direction == 'right':
            col += 1
        elif direction == 'left':
            col -= 1
        elif direction == 'up':
            row -= 1
        elif direction == 'down':
            row += 1
        # 인덱스를 벗어 났을 때
        if row >= n:
            row -= 1
            is_out_of_index = True
        elif row < 0:
            row += 1
            is_out_of_index = True
        elif col >= n:
            col -= 1
            is_out_of_index = True
        elif col < 0:
            col += 1
            is_out_of_index = True
        # 방향을 바꿔야할 때
        # 위의 두 if문을 통과한 row, col 기준 값이 있다면
        # 1. 벽에 부딪힌 경우에
        # 2. 이미 채워진 칸의 경우 (방향을 바꾸기전, 뒤로 한칸 뒤돌아 가야함)
        if answer[row][col]:
            if is_out_of_index:
                if direction == 'right':
                    row += 1
                    direction = 'down'
                elif direction == 'left':
                    row -= 1
                    direction = 'up'
                elif direction == 'up':
                    col += 1
                    direction = 'right'
                elif direction == 'down':
                    col -= 1
                    direction = 'left'
            else:
                if direction == 'right':
                    col -= 1
                    row += 1
                    direction = 'down'
                elif direction == 'left':
                    col += 1
                    row -= 1
                    direction = 'up'
                elif direction == 'up':
                    col += 1
                    row += 1
                    direction = 'right'
                elif direction == 'down':
                    col -= 1
                    row -= 1
                    direction = 'left'

        # 모든 작업이 끝나면 +1
        num += 1

    return answer


print(solution(4))