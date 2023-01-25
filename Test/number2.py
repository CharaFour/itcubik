x1 = int(input("Введите координаты первой клетки по X"))
y1 = int(input("Введите координаты первой клетки по Y"))
x2 = int(input("Введите координаты второй клетки по X"))
y2 = int(input("Введите координаты второй клетки по Y"))

state1 = "Неизвестно"
state2 = "Неизвестно"


if x1 == y1 and x2 == y2:
    state1 = "YES"
else:
    if x1 % 2 != y1 % 2 and x2 % 2 != y2 % 2:
        state1 = "YES"
    elif x1 % 2 == y1 % 2 and x2 % 2 == y2 % 2:
        state1 = "YES"
    else:
        print("NO")