from distutils.log import error
import random
a = int(input())
b = int(input())
if(abs(a-b)<=1):
    print('no integer between two numbers')
else:
    print(random.randrange(a,b))
    