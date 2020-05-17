import os
import numpy as np

import matplotlib.pyplot as plt
from utils import hex2color

class Animation:

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
            time = delay
        return animation

    def show(self, animation, resolution):

        figure = plt.figure()
        figure.canvas.draw_idle()
        dataEmpty = np.zeros(resolution)
        image = plt.imshow(dataEmpty)
        plt.show(block=False)

        for frame in animation:

            delay = frame["time"]
            if delay > 0:
                plt.pause(delay/1000)

            data = frame["data"]
            for i, row in enumerate(data):
                for j, value in enumerate(data[i]):
                    data[i][j] = hex2color('#' + value)

            image.set_data(np.array(data))
            plt.draw()

        plt.show(block=True)