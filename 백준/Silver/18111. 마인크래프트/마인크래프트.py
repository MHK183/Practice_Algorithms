import sys

input = sys.stdin.readline

if __name__ == '__main__':
    N, M, B = map(int, input().split())

    blocks = []
    for _ in range(N):
        blocks.extend(list(map(int, input().split())))

    # 현재 블록의 최소높이 미만, 최대높이 초과하는 경우를 탐색할 필요는 없다.
    min_h = min(blocks)
    max_h = max(blocks)
    # 초기화
    answer_time = (500 ** 2) * 256 * 2 # 이론상 걸릴 수 있는 최대 시간으로 초기화 if문으로 더 작은 값을 비교해 삽입하기 위함
    answer_height = 0

    for target_h in range(min_h, max_h + 1):
        time = 0
        have_blocks = B
        for block_h in blocks:
            diff = block_h - target_h
            have_blocks += diff
            if diff < 0:
                time += abs(diff)
            else:
                time += diff * 2

        if have_blocks < 0:
            continue

        if time <= answer_time:
            answer_time = time
            answer_height = target_h

    print(answer_time, answer_height)
