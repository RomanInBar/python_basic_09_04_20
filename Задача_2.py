time = input('Введите количество секунд - ')
while True:
    if time.isdigit():
        time = int(time)
        break
    else:
        time = input('Вы ввели не число. \nВведите количество секунд - ')


seconds = time
seconds = int(seconds)
minutes = time // 60
minutes = int(minutes)
hours = minutes // 60
hours = int(hours)

if seconds >= 60 or seconds % 60 == 0:
    seconds = time - (minutes * 60)

if minutes >= 60 or minutes % 60 == 0:
    minutes = minutes % 60

if hours >= 24:
    time = time - 86400
    hours = time // 3600

print(f'Время - {hours}:{minutes}:{seconds}')


