a,b,c,d = input("네 수를 입력하세요 : ").split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
u= (a+b+c+d)/4
print("평균 :",u)
print("분산 :",((a-u)**2+(b-u)**2+(c-u)**2+(d-u)**2)/4)