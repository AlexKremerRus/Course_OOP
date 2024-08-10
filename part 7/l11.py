from abc import ABC, abstractmethod

# abstract class for drawing
class Draw(ABC):
    @abstractmethod
    def draw(self,x,y):
        pass

# abstarct class for platform
class Platform(ABC):
    @abstractmethod
    def draw_shape(self, shape):
        pass

# realisation class Pen
class PenTool(Draw):
    def draw(self, x, y):
        print(f"Drawing PenTool at {x}, {y}")

# realisation class Brush
class BrushTool(Draw):
    def draw(self, x, y):
        print(f"Drawing BrushTool at {x}, {y}")

class PlatfomWindows(Platform):
    def draw_shape(self, shape):
        print(f"Drawing {shape} on Windows")

class PlatfomLinux(Platform):
    def draw_shape(self, shape):
        print(f"Drawing {shape} on Linux")

class PlatfomMac(Platform):
    def draw_shape(self, shape):
        print(f"Drawing {shape} on Mac")


class Canvas:
    def __init__(self, platform: Platform):
        self.platform = platform

    def draw_shape(self, tool: Draw, x, y):
        tool.draw(x, y)
        self.platform.draw_shape(type(tool).__name__)

if __name__ == "__main__":

    windows = PlatfomWindows()
    linux = PlatfomLinux()
    mac = PlatfomMac()

    penTool = PenTool()
    brushTool = BrushTool()

    canvas_windows = Canvas(windows)
    canvas_windows.draw_shape(penTool, 0, 10)
    canvas_windows.draw_shape(brushTool, 10, 20)

    canvas_linux = Canvas(linux)
    canvas_linux.draw_shape(brushTool, 10, 20)

    canvas_mac = Canvas(mac)
    canvas_mac.draw_shape(penTool, 20, 10)
