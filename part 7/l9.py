import random

from dataclasses import dataclass

first_name = ["Alex", "Sophie", "Mia", "Liam", "Noah"]
last_name = ["Smith", "Johnson", "Williams", "Brown", "Jones"]

@dataclass
class UserDataStorage:
    first_name = []
    last_name = []
    age = []

class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return( f"{self.first_name} {self.last_name} is {self.age} years old")

class SavingUser:
    def __init__(self, first_name, last_name, age, storage):
        self.storage = storage
        self.first_name_index = self.get_index_from_storage(first_name, self.storage.first_name)
        self.last_name_index = self.get_index_from_storage(last_name, self.storage.last_name)
        self.age_index = self.get_index_from_storage(age, self.storage.age)

    def get_index_from_storage(self, search_valiable, storage_savef_attr):
        if search_valiable in storage_savef_attr:
            return storage_savef_attr.index(search_valiable)
        else:
            storage_savef_attr.append(search_valiable)
            return len(storage_savef_attr) - 1


    def __str__(self):
        return f"{self.storage.first_name[self.first_name_index]} {self.storage.last_name[self.last_name_index]} is {self.storage.age[self.age_index]} years old"


if __name__ == "__main__":
    data_storage = UserDataStorage()

    users = [
        User(first_name=random.choice(first_name), last_name=random.choice(last_name), age = random.randint(18, 100) )

        for _ in range(1000)
    ]

    saving_user = [
        SavingUser(first_name=random.choice(first_name), last_name=random.choice(last_name), age = random.randint(18, 100), storage=data_storage )
    for _ in range(1000)
    ]

    result = f"First Name: {len(data_storage.first_name)} \n" + \
    f"Last Name: {len(data_storage.last_name)} \n" + \
    f"Age: {len(data_storage.age)}"
    print(result)
