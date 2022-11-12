list_a = []
for i in range(9):
    a = int(input())
    list_a.append(a)
    
max_value = 0
    
for idx, _ in enumerate(list_a):
    if list_a[idx] > max_value:
        max_value = list_a[idx]
        count = idx + 1
print(max_value)
print(count)