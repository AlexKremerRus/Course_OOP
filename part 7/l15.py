class VideoConverter:
    def convert(self, format):
        print(f"Converting video to {format} format...")

class VideoResizer:
    def resize(self, width, height):
        print(f"Resizing video to {width}x{height}...")

class VideoWatermarker:
    def add_watermark(self, text):
        print(f"Adding watermark '{text}' to video...")

class VideoProcessorFacade:
    def __init__(self):
        self.converter = VideoConverter()
        self.resizer = VideoResizer()
        self.watermarker = VideoWatermarker()

    def process_video(self, format, width, height, watermark_text):
        self.converter.convert(format)
        self.resizer.resize(width, height)
        self.watermarker.add_watermark(watermark_text)


if __name__ == "__main__":

    processor = VideoProcessorFacade()
    processor.process_video("mp4", 640, 360, "My Watermark")
