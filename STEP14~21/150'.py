x, y = input('x,y의 형태로 좌표를 입력하세요:').split(',')
x ,y = int(x), int(y)
print(x,y)
# x= int(input('enter x'))
# y = int(input('enter y'))

if (x>50 and x<100) &(y>40 and y<80):
    print('안에 있어요.')
else:
    print('밖에 있어요.')
