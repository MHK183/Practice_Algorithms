input()
n = sorted(map(int, input().split()))

input()
m = list(map(int, input().split()))

for i in m:
    answer = 0
    first, last = 0, len(n) - 1
    while first <= last:
        mid = (first + last) // 2
        if n[mid] < i:
            first = mid + 1
        elif n[mid] > i:
            last = mid - 1
        else:
            answer = 1
            break
    print(answer)
        
            
            