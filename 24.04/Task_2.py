# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

file = open('strings.txt', 'r', encoding='UTF-8')
strings = 0
while True:
    content = file.readline()
    if not content:
        break
    strings += 1
    print(f'Слов в {strings} строке - {len(content.split())}')
print(f'Строк в файле - {strings}')
file.close()
