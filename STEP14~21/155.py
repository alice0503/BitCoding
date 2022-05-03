num = int(input('하나의 정수를 입력하세요: '))
print('음수') if num<0 else print('양수')
print('홀수') if num%2==1 else print('짝수')
print('5의 배수') if num%5==0 else print('5의배수 아님')
