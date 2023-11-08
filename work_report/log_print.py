import datetime


class Log:
    is_print_log = 1

    def __init__(self, is_print_log):
        self.is_print_log = is_print_log

    def d(self, tag, value):
        if self.is_print_log == 0:
            return

        self.save_to_log_file(f"{tag} = {value}")

    def info(self, message):
        if self.is_print_log == 0:
            return
        self.save_to_log_file(message)

    @staticmethod
    def info_out(message):
        print(message)

    @staticmethod
    def info_out_to_file(time, message, log_file):
        print(time, message, file=log_file)

    @staticmethod
    def save_to_file(message, log_file):
        print(message, file=log_file)

    @staticmethod
    def save_to_log_file(message):
        now = datetime.datetime.now()
        today_log_name = f"{now.strftime('%Y-%m-%d')}_log.txt"
        with open(today_log_name, "a+", encoding="utf8") as log_file:
            print(message, file=log_file)

