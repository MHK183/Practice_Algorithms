import sys

test_case = int(sys.stdin.readline().rstrip())

for _ in range(test_case):
    scores = [int(i) for i in input().split()]
    scores_avg = sum(scores[1:]) / (len(scores) - 1)
    count = 0
    for i in scores[1:]:
        if i > scores_avg:
            count += 1
    print("{:.3f}%".format(count / (len(scores) -1 ) * 100))