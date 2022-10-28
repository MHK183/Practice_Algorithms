n = int(input())
fn = [0, 1]
for i in range(n):
    fn.append(fn[i] + fn[i+1])
print(fn[n])