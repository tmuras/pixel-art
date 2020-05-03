import os
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.colors as colors

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

    def __hex2color(self, hex):
        color = colors.hex2color(hex)
        return (int(color[0] * 255), int(color[1] * 255), int(color[2] * 255))

    def showAnimation(self, animation):

        figure = plt.figure()
        figure.canvas.draw_idle()
        dataEmpty = np.zeros((1, 1))
        image = plt.imshow(dataEmpty)
        plt.show(block=False)

        previousTime = 0

        for frame in animation:

            currentTime = frame["time"] / 1000
            delay = int(currentTime - previousTime)
            previousTime = currentTime

            if delay > 0:
                plt.pause(delay)

            data = frame["data"]
            for i, row in enumerate(data):
                for j, value in enumerate(data[i]):
                    data[i][j] = self.__hex2color('#' + value)

            image.set_data(np.array(data))
            plt.draw()

        plt.show(block=True)