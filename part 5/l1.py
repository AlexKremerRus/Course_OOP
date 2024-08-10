from abc import ABCMeta, abstractmethod
class Users(metaclass = ABCMeta):
    @abstractmethod
    def go_to(self):
        pass
    @abstractmethod
    def read(self):
        pass

class Test(Users):
    pass