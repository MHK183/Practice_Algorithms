# 한수 -> 1~99, 123, 135, 147,
def hansu(n):
    count = 0
    for i in range(1, n + 1):

        if i < 100:
            count += 1
        elif i < 1000:
            a, b, c = map(int, str(i))
            if (b-a) == (c-b):
                count += 1
        else:
            continue
    return count


k = int(input())
print(hansu(k))