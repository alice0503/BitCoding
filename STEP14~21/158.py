import random
n = random.randrange(1,100)
while True:
    ans1 = input('Guess number (Q to exit)')
    if ans1.upper == 'Q':
        break
    ans2 = int(ans1)
    if (n==ans2):
        print('Correct!')
        break
    elif(n>ans2):
        print('Choose higher number')
    else:
        print('Choose lower number')