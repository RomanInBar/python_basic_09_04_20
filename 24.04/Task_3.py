# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

file = open('staff.txt', 'r', encoding='UTF-8')
salary = 0
strings = 0
while True:
    string = file.readline()
    if not string:
        break
    strings += 1
    last_name = list(string.split())
    salary += int(last_name[-1])
    if int(last_name[-1]) < 20000:
        print(last_name[0])
print(f'Средняя величина дохода сотрудника - {salary/strings}')
file.close()



