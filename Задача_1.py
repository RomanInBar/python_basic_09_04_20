val_1 = input('Введите число - ')
val_2 = input('Введите ещё одно число - ')
while True:
    if val_1.isdigit() and val_2.isdigit():
        print(val_1, val_2)
        break
    else:
        val_1 = input('Вы ввели не число, введите число - ')
        val_2 = input('Ещё одно - ')

val_3 = input('Введите строку - ')
val_4 = input('Введите ещё одну строку - ')
print(val_3)
print(val_4)
