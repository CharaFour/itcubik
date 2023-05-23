mass = int(input("Введите массу: "))
height = int(input("Введите свой рост в метрах: "))

bmi = mass / height**2

if bmi < 18.5:
    print("Недостаточная масса")
elif bmi > 25:
    print("Избыточная масса")
else:
    print("Оптимальная масса")