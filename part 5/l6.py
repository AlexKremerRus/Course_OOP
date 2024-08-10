import time

class Monitor:
    def __init__(self, func):
        self.func = func
        self.get_time()

    def get_time(self):
        start_time = time.time()
        self.func()
        end_time  = time.time()
        print(f"result - {end_time - start_time}")

@Monitor
def handler():
    for i in range(5):
        print(f"handler - {i}")
        time.sleep(1)