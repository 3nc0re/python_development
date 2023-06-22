class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg
        self.log_error(msg)
    def log_error(self, msg):
        with open('logs/logs.txt', 'a') as file:
            file.write(f'{msg}\n')