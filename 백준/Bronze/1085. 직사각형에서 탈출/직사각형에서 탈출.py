x, y, w, h = map(int, input().split())
# x, y는 각각 w, h보다 항상 같거나 작음
distances = [x, y, w-x, h-y]

print(min(distances))