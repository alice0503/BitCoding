num = input('Enter the number: ')
numbers = ['1','2','3','4','5','6','7','8','9','0']
num_dot=0
isNum=True
for i in num:
    if not(i in numbers):
        if i =='.':
            num_dot +=1
            if num_dot==2:
                isNum = False
                break
        else:
            isNum = True
            break
print(num + ' is numbers?', isNum)
