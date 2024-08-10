class User:
    def __init__(self, name='Alex', age =20 ):
        self.name = name
        self.age = age
    def get_data(self):
        print(self.name)
        print(self.age)
    @staticmethod
    def get_sum(x,y):
        print(x+y)


class StringUtils:
    # @staticmethod
    def reverse_string(string):
        return string[::-1]

    def get_title(string):
        return string.title()

text ="hello"
print(StringUtils.get_title(text))