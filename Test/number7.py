x1 = int(input("Введите X первой клетки: "))
y1 = int(input("Введите Y первой клетки: "))
x2 = int(input("Введите X второй клетки: "))
y2 = int(input("Введите Y второй клетки: "))

if x2 - x1 == 2 or x2 - x1 == 1 and y2 - y1 == 1 or y2 - y1 == 2:
    print("YES")
elif x1 - x2 == 2 or x1 - x2 == 1 and y1 - y2 == 1 or y1 - y2 == 2:
    print("YES")