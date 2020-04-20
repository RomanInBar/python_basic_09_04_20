# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def info_person(name, last_name, age, city, email, tel):
    print(f'name-{name}, last_name-{last_name}, age-{age}, city-{city}, email-{email}, tel-{tel}')


info_person(name='Roman', last_name='Barabin', age='20.06.1994', city='Moscow', email='yamdex@mail.ru', tel='4567895')
