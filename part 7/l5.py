import copy


class TelegramUser:
    def __init__(self, user_name, user_file):
        self.user_name = user_name
        self.user_file : TelegramUserStorage = user_file

    def __str__(self):
        return f"{self.user_name}: {self.user_file}"


class TelegramUserStorage:
    def __init__(self, *args):
        self.file : tuple = args

    def __str__(self):
        return f'{", ".join(self.file)}'

if __name__ == "__main__":
    cache_file = ['file1', 'file2', 'file3']
    user_1 = TelegramUser(user_name = 'user1', user_file= TelegramUserStorage(*cache_file))

    user_2 = copy.deepcopy(user_1)

    user_1.user_name = 'test'
    user_1.user_file.file = ("1", "2", "3")

    print(user_1)
    print(user_2)