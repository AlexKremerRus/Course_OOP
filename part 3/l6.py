import webbrowser


class Test:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        webbrowser.open('https://google.com')
        return self.value + other
    def __sub__(self, other):
        return self.value - other
    def __eq__(self, other):
        if self.value == other:
            return True
        else:
            return False
    def __hash__(self):
        print("hash")
        return hash(self.value)