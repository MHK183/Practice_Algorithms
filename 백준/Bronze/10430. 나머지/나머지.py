num = list(map(int, input().split()))
a, b, c = num[0], num[1], num[2]
print(( a + b ) % c )
print((( a % c ) + ( b % c )) % c )
print(( a * b ) % c )
print((( a % c ) * ( b % c )) % c )