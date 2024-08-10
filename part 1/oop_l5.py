class User:
    def __init__(self, name="Alex") -> None:
        self._name = name   # _name - приватный аттрибут
    @property    # @property - декоратор для аттрибута который делает более безовасным код (секьюрным)
    def name(self):
        print("аттрибут выведен")
        return (self._name)
    @name.setter # @name.setter - декоратор для аттрибута, который устанавливает значение
    def name(self, value):
        print("аттрибут установлен")

        self._name = value

    @name.deleter # @name.deleter - декоратор для аттрибута, который удаляет значение
    def name(self):
        print("аттрибут удален")
        del self._name