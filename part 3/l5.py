class User:

    def __init__(self):
        print("__init__")
        self.arrage = [1,2,3,4]

    def __enter__(self):
        print("__enter__")
        return self.arrage

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        del self.arrage

a=User()
