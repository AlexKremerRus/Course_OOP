class Test:
    def __init__(self, arrage = [1,2,3,4]):
        self.arrage = arrage
    def __getitem__(self, index):
        return self.arrage[index]
    def __setitem__(self, index, value):
        self.arrage[index] = value
        print("установили значение")

    def __delitem__(self, index):
        del self.arrage[index]
        print("удалили значение")