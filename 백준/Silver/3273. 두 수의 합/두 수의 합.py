cnt = 0
n = int(input())
sequence = list(map(int, input().split()))
target = int(input())
left, right = 0, len(sequence) - 1
sequence.sort()

while not left == right:
    if sequence[left] + sequence[right] < target:
        left += 1
    elif sequence[left] + sequence[right] > target:
        right -= 1
    else:
        cnt += 1
        right -= 1
print(cnt)
        