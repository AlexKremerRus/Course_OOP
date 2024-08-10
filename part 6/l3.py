from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        raise NotImplementedError("Method needs to be implemented!")

class Dog(Animal):
    def speak(self):
        return f"{self.__class__.__name__} - Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.__class__.__name__} - Meow!"

def speak(animal):  # функция принимает экземпляр класса Animal
    print(animal.speak())

if __name__ == "__main__":
    dog = Dog()
    cat  = Cat()
    speak(dog)
    speak(cat)
