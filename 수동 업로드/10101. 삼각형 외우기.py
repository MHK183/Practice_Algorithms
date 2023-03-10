#!/usr/bin/env python
# coding: utf-8

# # 문제 10101. 삼각형 외우기
# 창영이는 삼각형의 종류를 잘 구분하지 못한다. 따라서 프로그램을 이용해 이를 외우려고 한다.
# 
# 삼각형의 세 각을 입력받은 다음, 
# 
# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error
# 를 출력하는 프로그램을 작성하시오.

# In[5]:


triangle = [int(input()) for _ in range(3)]

if triangle.count(60) == 3:
    print('Equilateral')
elif sum(triangle) == 180 and len(set(triangle)) == 2:
    print('Isosceles')
elif sum(triangle) == 180 and len(set(triangle)) == 3:
    print('Scalene')
else:
    print('Error')

