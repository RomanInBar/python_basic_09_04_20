# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix.
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, *args):
        self.numbers = args
        if len(args) == 6:
            self.matrix = [list(args[:2]), list(args[2:4]), list(args[4:])]
        elif len(args) == 8:
            self.matrix = [list(args[:4]), list(args[4:])]
        elif len(args) == 9:
            self.matrix = [list(args[:3]), list(args[3:6]), list(args[6:])]

    def __str__(self):
        print(f'Матрица: {self.matrix}')

    def __add__(self, other):
        result = list(map(lambda a, b: a + b, self.numbers, other.numbers))
        if len(result) == 6:
            return [result[:2], result[2:4], result[4:]]
        elif len(result) == 8:
            return [result[:4], result[4:]]
        elif len(result) == 9:
            return [result[:3], result[3:6], result[6:]]


m_1 = Matrix(1, 2, 3, 4, 5, 6)
m_2 = Matrix(7, 8, 9, 1, 2, 3)
m_1.__str__()
print(m_1 + m_2)
