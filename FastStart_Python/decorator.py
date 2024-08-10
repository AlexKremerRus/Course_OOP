
def make_cool(func):
    def wrapper():
        print("I am cool")
        func()
    return wrapper

@make_cool
def func():
    print("I am a function")
    return None


func()
