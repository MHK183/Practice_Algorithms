numbers = list(map(int, input().split()))
val_num = 0
for number in numbers:
    val_num += number**2
print(val_num%10)