score_board = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

score_total = 0
credit_total = 0

for _ in range(20):
    _, credit, score = input().split()

    if score == 'P':
        continue

    score_total += float(credit) * score_board[score]
    credit_total += float(credit)

print(f"{round(score_total / credit_total, 6):.6f}")