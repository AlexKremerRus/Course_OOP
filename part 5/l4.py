from typing import Any


class NoInstance(type):
    def __call__(self, *args, **kwds):
        raise TypeError("Не возможно создать экземпляр")


class Test(metaclass=NoInstance):
    def test(self):
        print("test")
