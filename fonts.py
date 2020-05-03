from pixels import Pixels
from PIL import Image, ImageDraw, ImageFont

class Fonts:

    def __init__(self, fontPath, size):

        self.font = ImageFont.truetype(fontPath, size)


    def getText(self, text, resolution, colour):
        width, height = resolution

        pixelsArray = []
        for sign in text:
            text_width, text_height = self.font.getsize(sign)
            image = Image.new('RGB', (text_width, text_height), (0, 0, 0))
            draw = ImageDraw.Draw(image)
            draw.text((0, 0), sign, colour, self.font)
            image = image.crop((0, text_height - height, width, text_height))
            letterPixels = Pixels(image)
            pixelArray = letterPixels.convert(resolution)
            pixelsArray.append(pixelArray)

        return pixelsArray