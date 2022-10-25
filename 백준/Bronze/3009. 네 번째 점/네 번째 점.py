coordinate_x = []
coordinate_y = []
fourth_xy = []
for _ in range(3):
    x, y = map(int, input().split())
    coordinate_x.append(x)
    coordinate_y.append(y)
for i in set(coordinate_x):
    if coordinate_x.count(i) == 1:
        fourth_xy.append(i)
for j in set(coordinate_y):
    if coordinate_y.count(j) == 1:
        fourth_xy.append(j)
print(fourth_xy[0], fourth_xy[1])