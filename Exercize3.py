# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons = ((1, 'Зима'), (2, 'Зима'), (3, 'Весна'), (4, 'Весна'), (5, 'Весна'), (6, 'Лето'), (7, 'Лето'), (8, 'Лето'), (9, 'Осень'), (10, 'Осень'), (11, 'Осень'), (12, 'Зима'))
seasons_dict = dict(seasons)
month = int(input("Введите число месяца: "))
if month in seasons_dict:
    print("Этот месяц входит в", seasons_dict[month])
else:
    print('Нет такого месяца')
#print(seasons_dict)
