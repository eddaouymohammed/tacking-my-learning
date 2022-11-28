import math
from math import *


print ('the equation is     AX°+BX+C=0')
a=int(input('A='))
b=int(input('B='))
c=int(input('C='))
#Y IS EQUAL THE DELTA  VALUE
y=(b**2)-4*a*c
print(y)
#CODITION USING IF ELSE 
if 0<y: 
    print('2 solution ')
    x1=(-b+sqrt(y))/2*a
    print (x1)
    x2=(-b-sqrt(y))/2*a
    print (x2)
if y==0:
    print ('one solution')
    x=(-b)/2*a
    print (x)
if y<0:
    print ('there is no solution ')
#done