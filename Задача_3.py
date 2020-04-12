n = input('Введите число "n" - ')
while True:
    if n.isdigit():
        break
    else:
        n = input('Вы ввели не число, введите число "n" - ')

n = int(n) + int(n*2) + int(n*3)
print('Ответ - ', n)