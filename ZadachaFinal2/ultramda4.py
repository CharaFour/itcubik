stringlst = input("Введите список чисел: ").split()
lst = [int(item) for item in stringlst]
newlst = []

newlst.append(lst[-1])
for i in range(len(lst) - 1):
    newlst.append(lst[i])
print(newlst)

