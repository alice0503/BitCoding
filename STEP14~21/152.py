colors = ['red','orange','blue','green','white','black','dark blue','purple']
color = input('Enter color: ')
if color in colors:
    print('Sorry')
else:
    colors.append(color)
    print(colors)