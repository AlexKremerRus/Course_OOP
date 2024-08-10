class Engine:
    def on(self):
        print("Engine on")

    def off(self):
        print("Engine off")

class Stereo:
    def rock(self):
        print("Stereo rock")


class Car:
    __engine = Engine()
    stereo = Stereo()

    def start(self):
        self.__engine.on()

    def music(self):
        self.stereo.rock()

    def stop(self):
        self.__engine.off()


lada = Car()
lada.start()
lada.music()
lada.stop()