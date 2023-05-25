first = input("Введите свой выбор: ").upper()
second = input("Введите свой выбор: ").upper()

if first == "КАМЕНЬ":
    if second == "КАМЕНЬ": print("Ничья")
    elif second == "БУМАГА": print("Победил Руслан")
    elif second == "НОЖНИЦЫ": print("Победил Тимур")
elif first == "БУМАГА":
    if second == "КАМЕНЬ": print("Победил Тимур")
    elif second == "БУМАГА": print("Ничья")
    elif second == "НОЖНИЦЫ": print("Победил Руслан")
elif first == "НОЖНИЦЫ":
    if second == "КАМЕНЬ": print("Победил Руслан")
    elif second == "БУМАГА": print("Победил Тимур")
    elif second == "НОЖНИЦЫ": print("Ничья")




