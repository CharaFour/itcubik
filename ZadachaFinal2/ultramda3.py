stringlst = input("Введите список чисел: ").split()
lst = [int(item) for item in stringlst]

for i in range(1, len(lst), 2):
    temp = lst[i]
    lst[i] = lst[i-1]
    lst[i-1] = temp
    
print(lst)