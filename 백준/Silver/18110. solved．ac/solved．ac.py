import sys
input = sys.stdin.readline


def round_half_up(num):
    float_num = num - int(num)
    if float_num >= 0.5:
        return int(num) + 1
    else:
        return int(num)


n = int(input())
answer = 0
if n > 0:
    diff_opinions = [int(input()) for _ in range(n)]

    sorted_diff_opinions = sorted(diff_opinions)
    # n명의 15%
    outlier = round_half_up(n * 0.15)

    # 가장 높은 15%, 낮은 15% 제외하기
    cut_opinions = sorted_diff_opinions[outlier:n-outlier]
    answer = round_half_up(sum(cut_opinions) / len(cut_opinions))
print(answer)

