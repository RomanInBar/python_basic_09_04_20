income = input('Выручка - ')
costs = input('Издержки - ')
if income.isdigit() and costs.isdigit():
    if int(income) > int(costs):
        profit = (int(costs) * 100) / int(income)
        profit = 100 - int(profit)
        print(f'Фирма работает с прибылью {profit}%.')
        staff = input('Введите количество сотрудников - ')
        profit_s = int(profit) / int(staff)
        print(f'Прибыль фирмы в расчете на одного сотрудника - {profit_s}%')
    else:
        print('Фирма работает в убыток')