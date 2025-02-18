class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def validate_email(line):
    name, email, years_old = line.split(' ')
    if line == " ":
        raise ValueError(f'Неверные данные {line}')

    name_is_valid = name.isalpha()
    if not name_is_valid:
        raise NotNameError(f"поле имени содержит НЕ только буквы - {name}, {line} ")

    email_is_valid = '.' in email and '@' in email
    if not email_is_valid:
        raise NotEmailError(f"поле емейл НЕ содержит @ и .(точку) - {email}, {line} ")

    years_old_is_valid = years_old.isdigit() and 10 <= int(years_old) <= 99
    if not years_old_is_valid:
        raise ValueError(f"поле возраст НЕ является числом от 10 до 99")


with open('registrations.txt', 'r', encoding='utf8') as ff, open('registrations_good.log.txt', 'w', encoding='utf8') as good_line, open(
        'registrations_bad.log', 'w', encoding='utf8') as bad_line:
    for line in ff:
        line = line[:-1]
        try:
            validate_email(line)
            good_line.write(f"{line}\n")

        except ValueError as e:
            bad_line.write(f" {line.strip()} Ошибка ValueError: {e}\n")

        except NotEmailError as e:
            bad_line.write(f" {line.strip()} Ошибка NotEmailError: {e}\n")

        except NotNameError as e:
            bad_line.write(f" {line.strip()} Ошибка NotNameError: {e}\n")


