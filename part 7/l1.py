import random

class DataBase:
    _instance = None

    # init лучше не юзать для синглтонов
    # def __init__(self):
    #     print(f"Init Id -{random.randint(1,100)} for {DataBase._instance}")

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DataBase, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    # def __str__(self):
    #     return f"DataBase - {self._instance}"

if __name__ == "__main__":
    db1 = DataBase()
    db2 = DataBase()
    print(db1)
    print(db2)
    print(f"{id(db1)} - db1 and {id(db2)} - db2")
    print(f"{hex(id(db1))} - db1 and {hex(id(db2))} - db2")
    print(f"{hex(id(db1)) == hex(id(db2))} - сравниваем")
