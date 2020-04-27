# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

file = open('number.txt', 'r', encoding='UTF-8')
list_1 = ['Один', 'Два', 'Три', 'Четыре']
i = 0
with open('rus_numbers', 'w', encoding='UTF-8') as file_1:
    while True:
        string = file.readline()
        if not string:
            break
        number = list(string.split())
        number[0] = list_1[i]
        i += 1
        number = ' '.join(number)
        print(number, file=file_1)
file.close()
