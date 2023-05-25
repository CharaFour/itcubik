stringlst = input("Введите список чисел: ").split()
lst = [int(item) for item in stringlst]
count = 0

for i in range(1, len(lst)): 
    if lst[i] > lst[i-1]: count += 1
        
print(count)