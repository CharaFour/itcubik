string = input("Введите строку: ")

cost = len(string) * 60

print(cost // 100, "р", end = '.')
print(cost % 100, "коп", end = '.')