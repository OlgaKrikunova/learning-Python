# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


class Counter:
    def __init__(self, file_name):
        self.file_open = file_name
        self.file = open(file_name, 'r')  # Открываем файл
        self.current_minute = None  # Исправили название переменной
        self.event_count = 0

    def __iter__(self):
        return self  # Итератор должен возвращать сам себя

    def __next__(self):
        for line in self.file:
            if "NOK" in line:
                timestamp = line.strip().split()[0]  # Берем только дату + время
                minute = timestamp[:16]  # Берем формат "YYYY-MM-DD HH:MM"
            else:
                continue
            if self.current_minute is None:
                self.current_minute = minute

            if minute == self.current_minute:
                self.event_count += 1
            else:
                result = (self.current_minute, self.event_count)  # Сохраняем текущий результат
                self.current_minute = minute  # Обновляем минуту
                self.event_count = 1  # Начинаем новый подсчет
                return result

        # Обрабатываем последний блок данных
        if self.event_count > 0:
            result = (self.current_minute, self.event_count)
            self.event_count = 0
            return result

        self.file.close()
        raise StopIteration  # Конец итерации

# ✅ Используем итератор
file_open = 'events.txt'

for minute, count in Counter(file_open):
    print(f"{minute} -> {count} событий")
