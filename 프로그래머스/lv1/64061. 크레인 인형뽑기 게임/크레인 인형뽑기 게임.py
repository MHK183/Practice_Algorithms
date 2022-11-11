def solution(board, moves):
    count = 0
    result = []
    for move in moves:
        
        for i in board:
            if i[move-1] != 0:
                result.append(i[move-1])
                i[move-1] = 0
                break
        while len(result) >= 2 and result[-1] == result[-2]:
            result.pop()
            result.pop()
            count += 2

    return count