# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

words = input('Введите несколько слов - ')
words = list(words.split(' '))
for i, word in enumerate(words):
    i+=1
    print(i, word[:10])


