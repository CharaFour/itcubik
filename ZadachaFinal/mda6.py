num = input()
newnum = ''

newnum = num[-3:]
num = num[0:-3]

while num != '':
    newnum = ',' + newnum
    newnum = num[-3:] + newnum
    num = num[0:-3]

print(newnum)

