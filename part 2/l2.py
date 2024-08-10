class USer:
    __slots__ = ['name', 'age']
    def __init__(self, name = 'name1', age = 20):
        self.name = name
        self.age = age


class User:

	def __init__(self, name):

		self.name = name

		print("working ", name)