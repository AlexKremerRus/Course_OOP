from functools import singledispatch

class User:
    def __init__(self, name = "name1"):
        self.name = name

    @singledispatch
    def get_value(value):
        print("default: ", value)
    @get_value.register(int)
    def _(value):
        print("int: ", value)
    @get_value.register(str)
    def _(value):
        print("str: ", value)