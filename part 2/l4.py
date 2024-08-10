class User:
    version = 1
    def __init__(self, name = "name1"):
        self.name = name
    @classmethod  # данная функция метод меняет аттрибут класса именно класса а не экземпляра
    def set_name(cls, value):
        cls.version = value