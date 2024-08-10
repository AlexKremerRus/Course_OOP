class Test:
    version =1

    def __init__(self, name= "name 1") :
        self.name = name
    @classmethod
    def rewrite(cls):
        cls.version = 2

a= Test(1)
b= Test(2)
a.rewrite()
print(f" a version : {a.version} / b version : {b.version} / class version : {Test.version}")