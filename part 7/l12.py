from abc import ABC, abstractmethod



# интерфейс для реализации компонентов

class IcomputerComponent(ABC):
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def name(self):
        pass

# класс создания компонентов
class Component(IcomputerComponent):
    def __init__(self, name, cost):
        self.__name = name
        self.__cost = cost

    def cost(self) -> int:
        return self.__cost

    def name(self) -> str:
       return self.__name


#
class ComposeComponent(IcomputerComponent):
    def __init__(self, name):
        self.__name = name
        self.components = []

    def cost(self) -> int:
        result_price = 0
        for component in self.components:
            component_price = component.cost()
            result_price += component_price
        return result_price

    def name(self) -> str:
        return self.__name

    def add_component(self, component: IcomputerComponent):
        self.components.append(component)

class PersonalComputer(ComposeComponent):
    def __init__(self, name : str):
        super().__init__(name)

    def cost(self):
        result_price = 0
        for component in self.components:
            component_price = component.cost()
            result_price += component_price
            print(f"price of {component.name()} is {component_price}")

            if type(component) == ComposeComponent:
                for detail in component.components:
                    print(f"\t - Price {detail.name()} is {detail.cost()}$")

        print(f"total price of {self.name()} is {result_price}")
        return result_price

if __name__ == '__main__':
    motherboard = ComposeComponent("Motherboard")
    motherboard.add_component(Component("CPU", 1000))
    motherboard.add_component(Component("GPU", 2000))
    motherboard.add_component(Component("RAM", 3000))


    computer_case =Component("case", 5000)
    storage = ComposeComponent("storage")
    storage.add_component(Component("SSD", 5000))


    pc = PersonalComputer("PC")
    pc.add_component(motherboard)
    pc.add_component(computer_case)
    pc.add_component(storage)
    pc.cost()