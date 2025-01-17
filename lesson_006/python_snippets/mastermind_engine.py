from random import randint

hidden_number = ''
box_result = {}


def guess_a_number():
    """загадать число"""
    global hidden_number
    numbers = []
    while len(numbers) < 4:
        number = str(randint(1, 9))
        if number not in numbers:
            numbers.append(number)
    hidden_number = ''.join(numbers)

    # return hidden_number


def check_number(num):
    """проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}"""
    global box_result
    box_result = {'bulls': 0, 'cows': 0}
    for i in range(4):
        if hidden_number[i] == num[i]:
            box_result['bulls'] += 1
        elif num[i] in hidden_number:
            box_result['cows'] += 1

    return box_result


def gameover():
    """конец игры"""
    if box_result == {'bulls': 4, 'cows': 0}:
        return hidden_number
    else:
        return False
