import math

for _ in range(int(input())):
    hak = 0
    score = 0
    for _ in range(int(input())):
        c, g = map(float, input().split())
        hak += c
        score += g * c
    print(int(hak), round(score / hak, 1))