class User:
    def __init__(self, name = 'Alex'):
        self.name = name
    def __len__(self):
        return len(self.name)
    def __str__(self):
        return self.name
    def __repr__(self): # данный дандер метод используется для отладки
        return f"{self.name} - objecct"
    def __del__(self):
        print("destructor")