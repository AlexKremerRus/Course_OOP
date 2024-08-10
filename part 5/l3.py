import sys

class ChangeMe:
    def __init__(self):
        local = sys._getframe(1).f_locals
        self.__dict__.update(
            (key, value) for key, value in local.items()
            if callable(value)
        )

def test1():
    print("test1")


def test2():
    print("test2")

a = ChangeMe()