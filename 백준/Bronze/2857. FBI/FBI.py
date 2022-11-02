names = [input() for _ in range(5)]
fbi = []
for idx, name in enumerate(names):
    if 'FBI' in name:
        fbi.append(idx+1)
if len(fbi) == 0:
    print("HE GOT AWAY!")
else:
    for i in fbi:
        print(i, end=' ')