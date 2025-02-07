class Log:
    def __init__(self, file_name):
        self.file_name = file_name
        self.parsed_logs = []
        self.grouped_by_day_logs = []

    def parse_logs(self):
        current_minute = ""
        count = 0
        with open(self.file_name, 'r') as file:
            for line in file:
                if line.endswith('NOK\n'):
                    minute = line[1:17]
                    if minute != current_minute:
                        if current_minute:
                            self.parsed_logs.append(f"[{current_minute}] {count}")
                        current_minute = minute
                        count += 1
                    elif minute == current_minute:
                        count += 1

    def write_file(self, out_file_name=None):
        if out_file_name is not None:
            file = open(out_file_name, 'w', encoding='utf8')
        else:
            file = None

        if file:
            file.writelines(f"{item}\n" for item in self.parsed_logs)
            file.close()


log = Log(file_name='events.txt')
log.parse_logs()
log.write_file(out_file_name='result.txt')
