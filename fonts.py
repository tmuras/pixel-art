from pixels import Pixels
from PIL import Image, ImageDraw, ImageFont

class Fonts:

    def __init__(self, fontPath, size):

        self.font = ImageFont.truetype(fontPath, size)


    def getText(self, text, resolution, colour):
        text_width, text_height = self.font.getsize(text)
        width, height = resolution
        image = Image.new('RGB', (text_width, text_height), (0, 0, 0))
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), text, colour, self.font)
        image = image.crop((0, text_height - height, text_width, text_height))

        pixelsArray = []
        for i in range(0, text_width, width + 1):
            box = (i, 0, i + width, height)
            letter = image.crop(box)
            letterPixels = Pixels(letter)
            pixelArray = letterPixels.convert(resolution)
            pixelsArray.append(pixelArray)

        return pixelsArray
