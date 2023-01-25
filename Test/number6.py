x1 = int(input("Введите X первой клетки: "))
y1 = int(input("Введите Y первой клетки: "))
x2 = int(input("Введите X второй клетки: "))
y2 = int(input("Введите Y второй клетки: "))

if x2 - x1 == y2 - y1:
    print("YES")
elif x1 + y1 == x2 + y2:
    print("YES")
else:
    print("NO")