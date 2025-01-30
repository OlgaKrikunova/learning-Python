from mastermind_engine import guess_a_number, check_number, gameover



print(f"Загадано число: {guess_a_number()}")
players_turn_in_the_game = 0
while True:
    num = input(f"Введите Ваш вариант:")
    players_turn_in_the_game += 1
    if len(num) != 4:
        print(f"Необходимо четырёхзначное число!")
        continue
    seen = set(list(num))
    if len(seen) != 4:
        print('Цифры не должны повторяться!')
        continue
    res = check_number(num)
    print(f"Проверка числа: быки - {res['bulls']}, коровы - {res['cows']}")
    if gameover():
        break

print(f"Победа! Количество ходов - {players_turn_in_the_game}. Хотите еще партию?")




