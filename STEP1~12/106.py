from audioop import reverse


sports = ['soccer']
print(sports)
sports.extend(['baseball','hockey'])
print(sports)
sports.insert(1,'tennis')
print(sports)
print(sorted(sports))
print(sports[1])
del(sports[0:2])
sports.reverse()
sports.insert(0,'soccer')
print(sports)

