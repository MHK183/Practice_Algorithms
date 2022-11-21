arr = []
for _ in range(9):
    row = list(map(int, input().split()))
    arr.append(row)
    
max_num = -1


for row, i in enumerate(arr):
    for col, j in enumerate(i):
        if max_num < j:
            max_num = j
            max_num_index = [row+1, col+1]
            
print(max_num)
print(max_num_index[0], max_num_index[1])