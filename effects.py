import numpy as np
from utils import rgb2hex
from structures import Structures

class Effects:

    def __init__(self, name=None, resolution=None, delay=None):

        self.effects = {}
        self.effects['snake_1'] = self.__snake1
        self.effects['snake_2'] = self.__snake2

        self.name = name
        if resolution != None:
            self.width, self.height = resolution
        self.delay = delay

    def list(self):
        return list(self.effects.keys())

    def get(self, colour):
        return self.effects[self.name](colour)

    def __snake1(self, colour):
        matrix = np.zeros([self.width, self.height], dtype=object)
        matrix.fill(rgb2hex((0, 0, 0)))
        pixelsArray = []

        i = 0
        j = 0
        iChange = 0
        jChange = 1
        iCounter = 0
        jCounter = 0
        counter = 1

        matrix[i][j] = rgb2hex(colour)
        pixelsArray.append(matrix.copy().tolist())

        while counter < self.width * self.height:

            i = i + iChange
            j = j + jChange
            counter = counter + 1
            matrix[i][j] = rgb2hex(colour)
            pixelsArray.append(matrix.copy().tolist())

            if j == self.height - 1 - jCounter and jChange == 1:
                jChange = 0
                iChange = 1
            elif i == self.width - 1 - iCounter and iChange == 1:
                jChange = -1
                iChange = 0
                iCounter = iCounter + 1
            elif j == jCounter and jChange == -1:
                jChange = 0
                iChange = -1
                jCounter = jCounter + 1
            elif i == iCounter and iChange == -1:
                jChange = 1
                iChange = 0

        return (pixelsArray, 50)

    def __snake2(self, colour):
        matrix = np.zeros([self.width, self.height], dtype=object)
        matrix.fill(rgb2hex((0, 0, 0)))
        pixelsArray = []

        i = 0
        j = 0
        jChange = 1
        counter = 1

        matrix[i][j] = rgb2hex(colour)
        pixelsArray.append(matrix.copy().tolist())

        while counter < self.width * self.height:

            j = j + jChange
            counter = counter + 1
            matrix[i][j] = rgb2hex(colour)
            pixelsArray.append(matrix.copy().tolist())

            if j == self.height - 1 and jChange == 1:
                jChange = 0
                i = i + 1
            elif j == 0 and jChange == -1:
                jChange = 0
                i = i + 1
            elif j == self.height - 1 and jChange == 0:
                jChange = -1
            elif j == 0 and jChange == 0:
                jChange = 1

        return (pixelsArray, 50)