from functools import singledispatch

class User:

    @singledispatch
    def get_number(value):
        print("default: ", value)
    @get_number.register(int)
    def _(value):
        return(100)
    @get_number.register(str)
    def _(value):
        return ("сто!")

print(User.get_number(1))