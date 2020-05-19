from pixels import Pixels
from PIL import Image, ImageDraw, ImageFont

class Fonts:

    def __init__(self, fontPath, size):

        self.font = ImageFont.truetype(fontPath, size)


    def __getImage(self, text, colour, resolution):
        height, width = resolution
        text_width, text_height = self.font.getsize(text)
        image = Image.new('RGB', (text_width, text_height), (0, 0, 0))
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), text, colour, self.font)
        if height != width:
            return image.crop((0, text_height - height, text_width, text_height))
        return image.crop((0, text_height - height, width, text_height))


    def getText(self, text, resolution, colour):
        height, width = resolution
        pixelsArray = []

        if width != height:
            image = self.__getImage(text, colour, resolution)
            textPixels = Pixels(image)
            for i in range(0, image.width + width):
                pixelArray = textPixels.convert(resolution, i)
                pixelsArray.append(pixelArray)
        else:
            for sign in text:
                image = self.__getImage(sign, colour, resolution)
                letterPixels = Pixels(image)
                pixelArray = letterPixels.convert(resolution)
                pixelsArray.append(pixelArray)

        return pixelsArray