D, H, W = map(int, input().split())

a = (D**2 / (H**2 + W**2))**(1/2)
print(int(H*a), int(W*a))