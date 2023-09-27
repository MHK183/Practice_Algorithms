N = int(input())
heights = list(map(int, input().split()))
current_bowman_height = heights[0]
kill_count = 0
best_kill = 0
for height in heights[1:]:

    if current_bowman_height > height:
        kill_count += 1
        if kill_count > best_kill:
            best_kill = kill_count
    elif current_bowman_height < height:
        current_bowman_height = height
        kill_count = 0

print(best_kill)