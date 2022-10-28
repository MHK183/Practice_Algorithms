n = int(input())
idx = 0
fn_1 = 1
fn_2 = 0
while n != idx:
    idx += 1
    
    fn = fn_2 + fn_1
    fn_2 = fn_1
    fn_1 = fn
    
print(fn_2)