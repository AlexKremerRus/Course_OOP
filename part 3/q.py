class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __hash__(self):
     return hash(self.name)
    def __eq__(self, other):
        return self.name == other.name
people = {}
people[Person('Alice', 30)] = 'Manager'
people[Person('Bob', 25)] = 'Engineer'
print(people)