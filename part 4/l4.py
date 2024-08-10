from typing import Any


class Test:
    # если атрибута не найдено взывается данный метод
    def __getattr__(self, atr):
        print("вызван несуществующий атрибут")

class Base:
    _ifield = []

    def __init__(self, *args):
        for name, value in zip(self._ifield, args):
            setattr(self, name, value)

class Stock(Base):
    _ifield = ["name", "shares", "price"]

    # def __init__(self, name, shares, price):
    #     self.name = name
    #     self.shares = shares
    #     self.price = price

a= Stock(1,2,3)

class Case:
    def __getattribute__(self, name):
        print(f"__getattribute__: {name}")
        return super().__getattribute__(name) # что значит тут супер??

class Test2(Case):
    def __init__(self,x):
        self.x = x

    def spam(self):
        pass



class TestDict(dict):
    def __setitem__(self, key, value):
        print("__setitem__")
        super().__setitem__(key, [value] * 3)

res = TestDict(a=1, b= 2)
print(res)

res["b"] = 22
print(res)