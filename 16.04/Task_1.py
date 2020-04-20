# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        print('Нельзя делить на ноль')


a = input('Введите первое число - ')
b = input('Введите второе число - ')
if a.isdigit() and b.isdigit():
    a = int(a)
    b = int(b)
print(division(a, b))
