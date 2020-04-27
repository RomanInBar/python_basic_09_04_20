# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран

with open('numbers.txt', 'w', encoding='UTF-8') as file:
    numbers = input('Введите числа через пробел - ')
    print(numbers, file=file)
file_1 = open('numbers.txt', 'r', encoding='UTF-8')
string = file_1.readline()
list_1 = sum([int(i) for i in string if i.isdigit()])
print(f'Сумма чисел - {list_1}')
file_1.close()
