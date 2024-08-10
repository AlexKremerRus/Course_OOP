class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

class ImageAdapter:
    def __init__(self, image):
        self.image = image

    def get_width_cm(self):
        dpi = 96  # дюймов на пиксель
        cm_per_inch = 2.54  # сантиметров на дюйм
        return self.image.get_width() / dpi * cm_per_inch

    def get_height_cm(self):
        dpi = 96  # дюймов на пиксель
        cm_per_inch = 2.54  # сантиметров на дюйм
        return self.image.get_height() / dpi * cm_per_inch

if __name__ == "__main__":



    image = Image(800, 600)
    adapter = ImageAdapter(image)

    print("Width:", adapter.get_width_cm())
    print("Height:", adapter.get_height_cm())
