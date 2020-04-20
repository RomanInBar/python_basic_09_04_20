# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

print('-'*75, 'Version №1', '-'*75)


def my_funk(x, y):  # Version №1
    result = x ** y
    return result


while True:
    x = input('Введите положительно ечисло - ')
    if x.isdigit() and int(x) > 0 and int(x) == float(x):
        x = int(x)
        break
while True:
    y = input('Введите целое отрицательное число - ')
    if int(y) < 0 and int(y) == float(y):
        y = int(y)
        break

print(my_funk(x, y))
print('-'*75, 'Version №2', '-'*75)


def my_funk(x, y):  # Version №2
    one = 1
    if y < 0:
        one = -one
    while y != 0:
        list_1.append(x)
        y -= one
    answer = 1
    for i in list_1:
        if one > 0:
            answer *= i
        if one < 0:
            answer /= i
    return answer


list_1 = []
while True:
    x1 = input('Введите положительно ечисло - ')
    if x1.isdigit() and int(x1) > 0 and int(x1) == float(x1):
        x1 = int(x)
        break
while True:
    y1 = input('Введите целое отрицательное число - ')
    if int(y1) < 0 and int(y1) == float(y1):
        y1 = int(y1)
        break

print(my_funk(x1, y1))
