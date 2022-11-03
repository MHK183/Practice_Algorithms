sum_move_time = 0

for _ in range(4):
    sum_move_time += int(input())
    
print(sum_move_time // 60)
print(sum_move_time % 60)