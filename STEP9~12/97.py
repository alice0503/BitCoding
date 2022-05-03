from xmlrpc.client import boolean


colors = ['red','yellow','blue']
print(colors)

print('yellow의 위치',colors.index('yellow'))
print('blue의 위치',colors.index('blue'))

colors.append('purple')
print(colors)

colors.insert(2,'pink')
print(colors)

colors.extend(['white','black'])
print(colors)

boolean = 'red' in colors
print(boolean)

boolean = 'orange' in colors
print(boolean)
