a = input('Киллометров за первый день - ')
b = input('Цель - ')
if a.isdigit and b.isdigit():
    a = int(a)
    b = int(b)
else:
    a = input('Введите количество киллометров за первый день - ')
    b = input('Введите цель - ')
day = 1
while True:
    print(f'{day}-й день: {round(a, 2)}')
    a = a + (a / 100 * 10)
    day+=1
    if a > b:
        print(f'{day}-й день: {round(a, 2)}')
        print(f'Ответ: на {day}-й день спортсмен достиг результата не менее 3 км.')
        break


