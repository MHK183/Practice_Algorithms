for i in range(int(input())):
    scores = list(map(int, input().split()))
    print(f'Class {i+1}')
    scores = sorted(scores[1:])
    score_gap = [scores[j+1] - scores[j] for j in range(len(scores) - 1)]
        
    print(f'Max {scores[-1]}, Min {scores[0]}, Largest gap {max(score_gap)}')