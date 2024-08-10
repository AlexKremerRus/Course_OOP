class User:
    def __init__(self, name):
        self.name = name
        print("working ", name)

class LocalUser:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        print(self.args)
        print(self.kwargs)

class TestA:
    def __init__(self, name):
        self.name = name
        self.get_name()

    def get_name(self):
        print(self.name)