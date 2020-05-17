import numpy as np
from utils import rgb2hex

class Effects:

    def __init__(self, name=None, resolution=None):

        self.effects = {}
        self.effects['snake_1'] = self.__snake1
        self.effects['snake_2'] = self.__snake2
        self.effects['rainbow'] = self.__rainbow

        self.name = name
        if resolution != None:
            self.height, self.width = resolution

    def list(self):
        return list(self.effects.keys())

    def get(self, parameter):
        return self.effects[self.name](parameter)

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

        return pixelsArray

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

        return pixelsArray

    def __rainbow(self, parameters):

        pixelsArray = []
        increment, iterations = parameters
        state = 0
        r = 255
        g = 0
        b = 0

        for i in range(0, iterations):
            matrix = np.zeros([self.width, self.height], dtype=object)
            matrix.fill(rgb2hex((r, g, b)))

            if state == 0:
                g = g + increment
                if g > 255 - increment:
                    state = 1
            if state == 1:
                r = r - increment
                if r < increment:
                    state = 2
            if state == 2:
                b = b + increment
                if b > 255 - increment:
                    state = 3
            if state == 3:
                g = g - increment
                if g < increment:
                    state = 4
            if state == 4:
                r = r + increment
                if r > 255 - increment:
                    state = 5
            if state == 5:
                b = b - increment
                if b < increment:
                    state = 0

            pixelsArray.append(matrix.copy().tolist())

        return pixelsArray
