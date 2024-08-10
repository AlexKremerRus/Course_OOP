class User:
    def __init__(self, name="name1"):
        self._name = name # _name - приватный аттрибут

class Test:
    def __init__(self,name = "name1"):
        self.__name = name # __name - защищенный аттрибут
    def __test(self):
        pass