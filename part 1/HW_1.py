class Product:
    version = 100

print(getattr(Product, 'version'))


class TestProduct:
    pass

setattr(TestProduct, 'version', 100)
print(getattr(TestProduct, 'version'))

class DelProduct:
    version = 100

print(f"ДО : {DelProduct.__dict__}  /")
delattr(DelProduct, 'version')
print(f"ПОСЛЕ : {DelProduct.__dict__}  /")


class User:

	def __init__(self, name="Alex"):

		self.name = name

		print("working ", name)

a=User()
print(a.name)
