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
    print('в январе 31 день')
elif month == 2:
    print('в феврале 28 дней')
elif month == 3:
    print('в марте 31 день')
elif month == 4:
    print('в апреле 30 дней')
elif month == 5:
    print('в мае 31 день')
elif month == 6:
    print('в июне 30 дней')
elif month == 7:
    print('в июле 31 день')
elif month == 8:
    print('в августе 30 дней')
elif month == 9:
    print('в сентябре 31 день')
elif month == 10:
    print('в октябре 30 дней')
elif month == 11:
    print('в ноябре 31 день')
elif month == 12:
    print('в декабре 30 дней')
else :
    print('номер некорректен')