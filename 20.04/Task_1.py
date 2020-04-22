# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


from sys import argv

_, hours, profit_hour, bonus = argv


def my_money(hs, ph, bs):
    profit = (int(hs) * int(ph)) + int(bs)
    return profit


print(my_money(hours, profit_hour, bonus))
