from typing import Any


class User:
    def __init__(self, value):
        self.value = value
    def __call__(self, comment):

        print(f"{self.value} - __call__")
        print(f"{comment} - comment")




class Test:
    def __iter__(self):
        print("__iter__")
        self.arrage = [1,2,3,4]
        return self

    def __next__(self):
        if self.arrage:
            return (f"__next__  {self.arrage.pop()}")
        else:
            raise StopIteration("self.arrage empty")

a=User(10)
b = Test()