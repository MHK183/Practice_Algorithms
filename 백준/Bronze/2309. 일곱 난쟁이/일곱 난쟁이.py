dwarf_heights = [int(input()) for _ in range(9)]
height_sum_error = sum(dwarf_heights) - 100
l = len(dwarf_heights)

for i in range(l-1):
    for j in range(i+1, l):
        if dwarf_heights[i] + dwarf_heights[j] == height_sum_error:
            dwarf_heights.remove(dwarf_heights[i])
            dwarf_heights.remove(dwarf_heights[j-1])
            break
    if sum(dwarf_heights) == 100:
        break
        
for dwarf_height in sorted(dwarf_heights):
    print(dwarf_height)
    
