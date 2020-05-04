# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


class Clothes:
    def __init__(self, height, size):
        self.height = height
        self.size = size

    @property
    def coat(self):
        return round(self.size / 6.5 + 0.5)

    @property
    def suit(self):
        return round(self.height * 2 + 0.3)

    def __add__(self):
        return round(self.coat + self.suit)


c = Clothes(1.71, 44)
print(c.coat)
print(c.suit)
print(c.__add__())


