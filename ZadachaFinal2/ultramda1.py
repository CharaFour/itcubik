amount = int(input("Введите кол-во точек: "))

first = 0
second = 0
third = 0
fourth = 0

for _ in range(amount):
    xy = input("Введитте координаты точки: ").split()
    if xy[0] > 0:
        if xy[1] > 0: first += 1
        elif xy[1] < 0: fourth += 1
    elif xy[0] < 0:
        if xy[1]> 0: second += 1
        elif xy[1] < 0: third += 1

print("I",first)
print("II",second)
print("III",third)
print("IV",fourth)