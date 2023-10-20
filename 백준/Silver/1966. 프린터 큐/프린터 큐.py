from collections import deque


def search():
    for doc in key_docs:
        if current_doc[1] < doc[1]:
            key_docs.popleft()
            key_docs.append(current_doc)
            return True
    return False


test_case = int(input())
for _ in range(test_case):
    N, M = map(int, input().split())

    docs = list(map(int, input().split()))
    key_docs = deque([(idx, priority) for idx, priority in enumerate(docs)])
    count = 0
    while True:
        current_doc = key_docs[0]

        is_higher = search()
        if is_higher:
            pass
        else:
            count += 1
            # 궁금한 문서 출력
            if current_doc[0] == M:
                print(count)
                break
            else:
                # 인쇄한다
                key_docs.popleft()
