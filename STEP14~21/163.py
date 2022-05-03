import random
min_num= 1
max_num=2
level=0
while level<3:
    level+=1
    ans=random.randrange(min_num,max_num)
    a= int(input('level{} ({} ~ {})'.format(level,min_num,max_num)))
    if a==ans:
        print('Correct!')
        max_num=max_num*2
    else:
        print('Failure!')
        print('answer is : ',ans)
        break
if max_num>8:
    print('Lucky!')

    
    

    

