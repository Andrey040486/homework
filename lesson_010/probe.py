# name, email, age = line.split(' ')
# age = int(age)
class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


with open('registrations.txt', 'r', encoding='utf8') as ff:
    for line in ff:
        line = line[:-1]
        try:
            name, email, age = line.split(' ')
            age = int(age)
        except ValueError as exc:

            if 'unpack' in exc.args[0]:
                print(f'Не хватает операндов {exc} в строке {line}')
            elif 10 > age > 99:
                print(f'поле {age} НЕ является числом от 10 до 99 в строке {line}')


