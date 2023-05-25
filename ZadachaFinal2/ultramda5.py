stringlst = input("Введите список чисел: ").split()
lst = [int(item) for item in stringlst]

lost = []

for i in lst:
    if i not in lost:
        lost.append(i)
print(len(lost))