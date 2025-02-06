import zipfile
from idlelib.iomenu import encoding
from pprint import pprint


class Statistics:
    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}

    def unpacking(self):
        zfile = zipfile.ZipFile(self.file_name, "r")
        for filename in zfile.namelist():
            zfile.extract(filename)

    def check(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self._check_for_line(line=line)

    def _check_for_line(self, line):
        for char in line:
            if char.isalpha():
                if char in self.stat:
                    self.stat[char] += 1
                else:
                    self.stat[char] = 1

    def console_output(self):
        for letter, count in sorted(self.stat.items()):  # Сортируем по алфавиту
            print(f"| {letter:^9} | {count:^9} |")
            print("_" * 25)

    def total(self):
        total = sum(self.stat.values())
        print(f"| {'Итого':^9} | {total:^9} |")

statistics = Statistics(file_name='voyna-i-mir.txt')

print(f"статистика по буквам в романе Война и Мир")
print()
print('+', '-' * 9, '+', '-' * 9, '+')
statistics.check()
statistics.console_output()
statistics.total()
print('+', '-' * 9, '+', '-' * 9, '+')




