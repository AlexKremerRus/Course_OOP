class TestClass:
    version =1

    def get_name(self):
        print("test")

class User:
    name = "Alex"
    age = 14
    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age)


class Ten(int):
    pass