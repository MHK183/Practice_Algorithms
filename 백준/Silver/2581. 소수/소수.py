m = int(input())
n = int(input())
numbers = [i for i in range(m, n+1)]
if 1 in numbers:
    numbers.remove(1)
prime_numbers = numbers.copy()
for number in numbers:

    for i in range(2, int(number**(1/2))+1):
        if number % i == 0:
            prime_numbers.remove(number)
            break

if len(prime_numbers) == 0:
    print(-1)
else:
    print(sum(prime_numbers))
    print(min(prime_numbers))