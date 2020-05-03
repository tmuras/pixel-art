import os
import numpy as np

class Structures:

    def __init__(self, *args):

            if len(args) == 1:
                self.pixelsArray, = args
            elif len(args) == 2:
                structuresFolder, name = args
                self.pixelsArray = []

                for filename in sorted(os.listdir(structuresFolder)):
                    if filename.startswith(name + "_"):
                        filePath = structuresFolder + filename
                        array = np.loadtxt(filePath, dtype="str", comments=None)
                        self.pixelsArray.append(array.tolist())


    def get(self, delay):
        animation = []
        time = 0
        for pixelArray in self.pixelsArray:
            row = {
                'time': time,
                'data': pixelArray
            }
            animation.append(row)
            time = time + delay
        return animation