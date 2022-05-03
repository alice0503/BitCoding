a,b,c = input('계산식을 입력하세요: ').split()
a,c=int(a),int(c)
if (b == '+'):
    print(a+c)
elif (b=='-'):
    print(a-c)
elif (b=='*'):
    print(a*c)
elif (b=="/"):
    print(a/c)