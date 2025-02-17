BRUCE_WILLIS = 42
input_data = None
try:
    input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
    leeloo = int(input_data[4])
    print(leeloo)
    result = BRUCE_WILLIS * leeloo
    print(f"- Leeloo Dallas! Multi-pass № {result}!")
except IndexError:
    print(f"Обращение к несуществующему индексу. "
          f"Введено -  '{input_data}'. Необходимо ввести более 5 символов!")

except ValueError:
    print(f"Операция получает аргумент неподходящего значения - '{input_data}'. "
          f"Нужно ввести целое число!")



