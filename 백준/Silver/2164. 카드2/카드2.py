from collections import deque


N = int(input())

cards = deque([card for card in range(1, N + 1)])
while len(cards) != 1:
    # 맨위 카드를 버린다
    cards.popleft()
    # 버린 후 맨위의 카드를 맨 아래로 넣는다
    cards.append(cards[0])
    cards.popleft()

print(cards[0])