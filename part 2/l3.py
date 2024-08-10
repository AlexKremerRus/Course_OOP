class Test:
    def __new__(cls, *args, **kwargs):
        print("create exampl class")
        instance = super().__new__(cls)
        return instance
    def __init__(self, name='alex'):
        print("init")
        self.name = name
