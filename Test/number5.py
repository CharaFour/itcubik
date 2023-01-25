chislo = int(input("Введите число:"))

if chislo % 2 == 1:
    print("YES")
elif 2 <= chislo <= 5:
    print("NO")
elif 6 <= chislo <= 20:
    print("YES")
elif chislo > 20:
    print("NO")
else:
    print("как")
