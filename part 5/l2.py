class Counter:
    def __init__(self,func):
        self.func = func
        self.count = 0
    def __call__(self,*args, **kwargs):
        self.count += 1
        print(f"{self.count} - {self.func.__name__}")
        return self.func(*args, **kwargs)

@Counter
def printer():
    print("hello")