

def generator(n):
    yield n

g = generator(10)
print(next(g))
print(next(g))