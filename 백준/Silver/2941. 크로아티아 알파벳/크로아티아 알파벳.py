# replace 사용해보기
croa = input()
croa_alpha = ['c=','c-','dz=','z=','d-','lj','nj','s=']

for i in croa_alpha:
    croa = croa.replace(i, "0")
print(len(croa))