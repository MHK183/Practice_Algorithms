def solution(board):
    board_size = len(board)**2
    bomb_index = []
    bomb_range = []
    
    # 폭탄 인덱스 저장
    for idx, i in enumerate(board):
        
        for n, k in enumerate(i):
            if k == 1:
                bomb_index.append((idx, n))
    # 폭탄 범위 인덱스 저장
    for x in bomb_index:
        for i in range(-1, 1 + 1):
            for j in range(-1, 1 + 1):
                bomb_range.append((x[0]+i, x[1]+j))
    answer = bomb_range.copy()
    
    for i in bomb_range:

        if i[0] < 0 or i[1] < 0 or \
            i[0] > len(board) -1 or \
            i[1] > len(board) -1:
            
            answer.remove(i)
    
    
    return board_size - len(set(answer))