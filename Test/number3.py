age = int(input("Введите свой возраст: "))
gender = input("Введите свой пол (m или f): ")

if gender == "m" or gender == "f":
    if gender == "f" and 10 <= age <= 15:
        print("YES")
    else:
        print("NO")
else:
    print("Гендеров всего 2, левачок")