def solution(n):
    pizza = 0
    while True:
        pizza += 1
        pizza_piece = 7 * pizza
        if pizza_piece >= n:
            return pizza