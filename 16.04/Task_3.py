# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_funk(a, b, c):
    numbers = [a, b, c]
    max_1 = max(numbers)
    if max_1 in numbers:
        numbers.remove(max_1)
    max_2 = max(numbers)
    result = max_1 + max_2
    return result


print(my_funk(3, 6, 9))
