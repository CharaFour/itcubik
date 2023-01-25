x1 = int(input("Введите X первой клетки: "))
y1 = int(input("Введите Y первой клетки: "))
x2 = int(input("Введите X второй клетки: "))
y2 = int(input("Введите Y второй клетки: "))

if x2 - x1 == 2 or x2 - x1 == -2:
    if y2 - y1 == 1 or y2 - y1 == -1:
        print("YES")
    else:
        print("NO")
elif x2 - x1 == 1 or x2 - x1 == -1:
    if y2 - y1 == 2 or y2 - y1 == -2:
        print("YES")
    else:
        print("NO")
else:
    print("NO")