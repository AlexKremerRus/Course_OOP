class Test:
    def get():
        print("get")

class Test2:

    def get():
        print("get2")

class Template(Test, Test2):
    def __init__(self, name):
        self.name = name

    def start(self):
        Test.get()
        Test2.get()