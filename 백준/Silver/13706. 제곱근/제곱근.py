N = int(input())
start, last = 0, N

while True:
    mid = (start + last) // 2
    if mid**2 > N:
        last = mid - 1
    elif mid**2 < N:
        start = mid + 1
    else:
        print(mid)
        break