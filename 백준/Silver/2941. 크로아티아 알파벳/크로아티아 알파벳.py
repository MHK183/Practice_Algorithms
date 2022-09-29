croa = input()
count = 0
croa_alpha = ['c=','c-','dz=','z=','d-','lj','nj','s=']
for i in croa_alpha:
    if i in croa:
        if i == 'z=':
            count += (croa.count(i) - croa.count('dz='))
        else:
            count += croa.count(i)
if croa.count('dz=') >= 1:
    print(len(croa) - count - croa.count('dz='))
else:
    print(len(croa) - count)