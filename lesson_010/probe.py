# name, email, age = line.split(' ')
# age = int(age)


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def registration(line):
    name, email, age = line.split(' ')
    name = str(name)
    email = str(email)
    if 10 > int(age) > 99:
        raise ValueError
    if not name.isalpha():
        raise NotNameError
    # if '@' and '.' in email is True:
    if email.find('.') == -1 and email.find('@') == -1:
        raise NotEmailError


with open('registrations.txt', 'r', encoding='utf8') as ff:
    for line in ff:
        line = line[:-1]
        try:
            registration(line=line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'Не хватает операндов {exc} в строке {line}')
            else:
                print(f'поле НЕ является числом от 10 до 99 в строке {line}')
        except NotNameError:
            print(f'поле имени содержит НЕ только буквы в строке {line}')
        except NotEmailError:
            print(f'поле емейл НЕ содержит @ и .(точку) в строке {line}')
