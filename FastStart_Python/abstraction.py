
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Figure):
    def area(self):
        pass

circle_1 = Circle()