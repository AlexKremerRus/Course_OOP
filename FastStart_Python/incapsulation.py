"""
в питоне нет нормальной инкапсуляции классов
"""

class Macbook:
    owner = None # public - можем менять
    _id = None # protected Не менять переменные - только при создании (но можем менять obj._id)
    __manufacturer = "Apple" # private - вообще никогда не менять - (но меняется через obj._Macbook__manufacturer)
    def __init__(self, _id):
        self._id= _id
# как получать приватные персенные
    def get_manufacturer(self):
        return self.__manufacturer

mac130 = Macbook(130)

mac130.__manufacturer = "HP"
print(mac130.__manufacturer)

print(mac130._Macbook__manufacturer)
mac130.owner = "Alex"
print(mac130.owner)


print(mac130.get_manufacturer())