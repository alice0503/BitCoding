a= int(input('first num : '))
b= int(input('second num : '))
if a>b:
    c=a
    a=b
    b=c
while a<=b:
    if a%5==0:
        print(a)
    a+=1
