x_all = ''
y_all = ''
colors = 1

with open("colors.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        x_all += line[0]
        y_all += line[2]
    f.close()

for i in range(1, len(x_all)):
    x = int(x_all[i])
    y = int(y_all[i])
    xp = int(x_all[i-1])
    yp = int(y_all[i-1])

    if not (x == xp or (x - 1 == xp or x + 1 == xp)):
        colors += 1
    else:
        if not (y == yp or (y - 1 == yp or y + 1 == yp)):
            colors += 1

print("Всего цветов нужно:", colors)