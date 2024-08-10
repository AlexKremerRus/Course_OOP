import random

def singleton(class_obj):
    _instances = {}

    def get_instance(*args, **kwargs):
        if class_obj not in _instances:
            _instances[class_obj] = class_obj(*args, **kwargs)
        return _instances[class_obj]

    return get_instance

@singleton
class Database:
    def __init__(self):
        print(f"Init Id -{random.randint(1,100)}")


if __name__ == "__main__":
    db1 = Database()
    db2 = Database()
    print(db1)
    print(db2)
    print(f"{id(db1)} - db1 and {id(db2)} - db2")
    print(f"{hex(id(db1))} - db1 and {hex(id(db2))} - db2")
    print(f"{hex(id(db1)) == hex(id(db2))} - сравниваем")
