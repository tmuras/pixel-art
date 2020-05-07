import numpy as np
import os
import sys
from utils import rgb2hex

class Test:

    filename = 'test.txt'
    path = os.path.dirname(sys.argv[0])
    filePath = path + "/data/" + filename

    def __init__(self, resolution):

        self.width, self.height = resolution


    def get(self):

        pixelsArray = []
        array = np.loadtxt(self.filePath, dtype="str", comments=None)
        pixelsArray.append(array.tolist())
        return pixelsArray


    def generate(self):

        pixelsArray = []
        matrix = np.zeros([self.width, self.height], dtype=object)
        colour = [0, 0, 0]

        for i in range(0, self.width):
            for j in range(0, self.height):
                colour = (int(colour[0]), int(colour[1]), int(colour[2]))
                matrix[i][j] = rgb2hex(colour)
                colour = np.random.uniform(low=0, high=255, size=(3))

        np.savetxt(self.filePath, matrix, fmt='%s')
        pixelsArray.append(matrix.copy().tolist())
        return pixelsArray

