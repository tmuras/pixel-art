from pixels import Pixels
from PIL import Image, ImageDraw, ImageFont

import math

class Fonts:

    def __init__(self, fontPath, size, effect, resolution):

        self.size = size
        self.effect = effect
        self.height, self.width = resolution

        if size == 'small':
            self.font = ImageFont.truetype(fontPath, self.height)
        else:
            self.font = ImageFont.truetype(fontPath, 2 * self.height)


    def __getImage(self, text, colour):
        text_width, text_height = self.font.getsize(text)
        width = text_width
        if text_width < self.width:
            width = self.width
        height = text_height
        if text_height < self.height:
            height = self.height
        image = Image.new('RGB', (width, height), (0, 0, 0))
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), text, colour, self.font)
        return image


    def getText(self, text, colour):
        pixelsArray = []
        resolution = (self.height, self.width)

        lines = None
        if self.effect == 'scroll':
            lines = [text.replace("|", " ")]
        else:
            lines = text.split("|")

        for line in lines:
            image = self.__getImage(line, colour)
            textPixels = Pixels(image)
            if self.effect == 'scroll':
                for i in range(0, image.width + self.width + 1):
                    columns = (i, i + self.width)
                    pixelArray = textPixels.convert(resolution, self.effect, columns)
                    pixelsArray.append(pixelArray)
            else:
                frameWidth, letterWidth = self.__getFrameWidth(line)
                frames = 1
                if frameWidth + letterWidth <= image.width:
                    frames = math.ceil(image.width / frameWidth)
                columns = (0, frameWidth)
                for i in range(0, frames):
                    pixelArray = textPixels.convert(resolution, self.effect, columns)
                    pixelsArray.append(pixelArray)
                    columns = (columns[0] + frameWidth, columns[1] + frameWidth)

        return pixelsArray


    def __getFrameWidth(self, text):
        letterWidth, letterHeight = self.font.getsize(text[0])
        letterCounter = 1
        while letterWidth * letterCounter < self.width:
            letterCounter = letterCounter + 1
        return (letterWidth * (letterCounter - 1), letterWidth)