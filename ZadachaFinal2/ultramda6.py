amount = int(input())

lst = []

true = False

for _ in range(amount):
    num = int(input("Введите числа: "))
    lst.append(num)

mnozh = int(input())

for i in lst:
    for j in lst:
        if j != i:
            if i * j == mnozh: true = True

if true: print("ДА")
else: print("НЕТ")



