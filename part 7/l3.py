class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass = Singleton):
    def __init__(self):
        print("Database init")

if __name__ == '__main__':
    db1 = Database()
    db2 = Database()
    print(db1)
    print(db2)
    print(f"{id(db1)} - db1 and {id(db2)} - db2")
    print(f"{hex(id(db1))} - db1 and {hex(id(db2))} - db2")
    print(f"{hex(id(db1)) == hex(id(db2))} - сравниваем")
