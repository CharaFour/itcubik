num = input()

lastnum = num[-1:-6:-1]
firstnum = num[:-5:1]

newnum = firstnum + lastnum
print(newnum)