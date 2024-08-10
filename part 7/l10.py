class TelegramUser:
    def __init__(self):
        print("Creating TelegramUser")

        #base info
        self.first_name = None
        self.username = None

        # limit
        self.limit_message = None
        self.limit_group = None


    def __str__(self):
        return f"First Name: {self.first_name}, Username: {self.username}; Message limit - {self.limit_message}; Group limit - {self.limit_group}"

class TelegramUserBuilder:
    def __init__(self, user=None):
        if user is None:
            self.user = TelegramUser()
        else:
            self.user = user

    def build(self):
        return self.user

class TelegramFirstNameBuilder(TelegramUserBuilder):
    def set_name(self, first_name):
        self.user.first_name = first_name
        return self

class TelegramUsernameBuilder(TelegramFirstNameBuilder):
    def set_username(self, username):
        self.user.username = username
        return self

class TelegramMessageLimitBuilder(TelegramUsernameBuilder):
    def set_limit_message(self, limit_message):
        self.user.limit_message = limit_message
        return self

class TelegramGroupLimitBuilder(TelegramMessageLimitBuilder):
    def set_limit_group(self, limit_group):
        self.user.limit_group = limit_group
        return self





if __name__ == "__main__":
    user_1 = TelegramGroupLimitBuilder() # ,ерем последний класс потому что в нем есть все функции и методы что описаны выше него


    user_1_result = user_1.set_name("Alex").set_username("@Al_Star").set_limit_message(100).set_limit_group(5).build()

    print(user_1_result)

    user_2 = TelegramUserBuilder().build()

    print(user_2)