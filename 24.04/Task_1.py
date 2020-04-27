# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


with open('string.txt', 'w', encoding='UTF-8') as file:
    while True:
        string = input('Введите строку: ')
        print(string, file=file)
        if not string:
            break
file.close()




