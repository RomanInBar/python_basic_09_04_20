val_1 = input('Введите число - ')
if val_1.isdigit() and int(val_1) > 0 and int(val_1) == float(val_1):
    val_2 = max(list(map(int, val_1)))
    print(val_2)


