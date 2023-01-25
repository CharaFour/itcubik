x1 = int(input("Введите координаты первой клетки по X"))
y1 = int(input("Введите координаты первой клетки по Y"))
x2 = int(input("Введите координаты второй клетки по X"))
y2 = int(input("Введите координаты второй клетки по Y"))

state1 = "Неизвестно"
state2 = "Неизвестно"


if x1 == y1:
    state1 = "Черная"
else:
    if x1 % 2 != y1 % 2:
        state1 = "Белая"
    elif x1 % 2 == y1 % 2:
        state1 = "Черная"

if x2 == y2:
    state2 = "Черная"
else:
    if x2 % 2 != y2 % 2:
        state2 = "Белая"
    elif x2 % 2 == y2 % 2:
        state2 = "Черная"

if state1 == state2:
    print("YES")
else:
    print("NO")