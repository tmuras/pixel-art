from PIL import Image, ImageSequence
import numpy as np
from utils import rgb2hex
import os

class Pixels:

    def __init__(self, *args):

        if len(args) == 1:
            self.image, = args
        elif len(args) == 2:
            imageFolder, filename = args
            filePath = imageFolder + filename
            self.filename = filename
            self.image = Image.open(filePath)


    def __prepareImage(self, image, resolution):
        image = image.convert('RGB')
        image = image.resize(resolution)
        return image

    def __convert(self, image, resolution):
        pixelValues = [rgb2hex(color) for color in image.getdata()]
        pixelArray = np.array(pixelValues, dtype='str').reshape(resolution)
        return pixelArray

    def save(self, resolution, outputFolder):

        index = 1
        for frame in ImageSequence.Iterator(self.image):
            file, ext = os.path.splitext(self.filename)
            outputFilePath = outputFolder + file + '_' + str(index) + '.txt'
            frame = self.__prepareImage(frame, resolution)
            pixelArray = self.__convert(frame, resolution)
            np.savetxt(outputFilePath, pixelArray, fmt='%s')
            index += 1

    def convert(self, resolution):
        pixelArray = self.__convert(self.image, resolution)
        return pixelArray.tolist()