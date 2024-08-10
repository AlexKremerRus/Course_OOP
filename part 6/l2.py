from abc import ABC, abstractmethod

class BaseTelegramUser(ABC):
    @abstractmethod
    def get_message_limit(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} {self.id}"
        # ввыод имени класса откуда вызвался метод
class FreeUser(BaseTelegramUser):
    def get_message_limit(self):
        return 30

class VipUser(BaseTelegramUser):
    def get_message_limit(self):
        return 100

class SuperUser(BaseTelegramUser):
    def get_message_limit(self):
        return 1000

if __name__ == '__main__':
    FreeUser = FreeUser()
    VipUser  = VipUser()
    SuperUser = SuperUser()
    