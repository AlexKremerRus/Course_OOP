class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age

class Database:
    def __init__(self, user: User):
        self.user = user

    def get_info(self):
        result = f"{self.user.username} is {self.user.age} years old"
        print(result)

class DatabaseProxy:
    def __init__(self, user: User):
        self.user = user
        self.database = Database(user)

    def get_info(self):
        if self.user.username.istitle():
            print(self.__class__.__name__)
            self.database.get_info()
        else:
            raise ValueError("Username error")

if __name__ == "__main__":
    db = Database(user= User("John", 30))
    db.get_info()

    db_small = Database(user = User("ivan", 22))
    db_small.get_info()

    db_proxy = DatabaseProxy(user= User("Kirill", 44))
    db_proxy.get_info()

    db_proxy_small = DatabaseProxy(user = User("ivan", 12))
    db_proxy_small.get_info()
