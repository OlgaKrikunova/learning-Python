# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

if month == 1:
    print('31')
elif month == 2:
    print('28')
elif month == 3:
    print('31')
elif month == 4:
    print('30')
elif month == 5:
    print('31')
elif month == 6:
    print('30')
elif month < -1:
    print('gfsgsh')
elif month == 0:
    print('sdgg')
else:
    print('klsdghghlagh;')
