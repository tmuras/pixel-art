#!/usr/bin/env python3

import sys
import os
import argparse
import json
from pixels import Pixels
from structures import Structures
from fonts import Fonts

# http://www.iconarchive.com
imagesFolder = "images/"
structuresFolder = "structures/"
# http://sharefonts.net
fontPath = "fonts/code.ttf"
resolution = (8, 8)


def main():

    path = os.path.dirname(sys.argv[0])

    imagesFolderPath = path + "/" + imagesFolder
    structuresFolderPath  = path + "/" + structuresFolder
    fontFullPath = path + "/" + fontPath

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--update', default=False, type=bool, help='Regenerate structures from existing images')
    parser.add_argument('--delay', default=1000, type=int, help='Set animation delay')
    parser.add_argument('--colour', default=(255, 255, 255), type=object, help='Set font colour')
    parser.add_argument('--image', help='Get structures for image')
    parser.add_argument('--text', help='Get structures for text')
    parser.add_argument('--images', help='Get all available images')


    args = parser.parse_args()

    if args.update == True:
        # http://www.iconarchive.com/show/arcade-saturdays-icons-by-mad-science/Bashfull-Inky-icon.html
        # http://www.iconarchive.com/show/square-animal-icons-by-martin-berube.html
        for filename in os.listdir(imagesFolderPath):
            pixels = Pixels(imagesFolderPath, filename)
            pixels.save(resolution, structuresFolderPath)

    if args.images != None:
        images = []
        for filename in os.listdir(structuresFolderPath):
            file, ext = os.path.splitext(filename)
            name = file.split("_")[0]
            if name not in images:
                images.append(name)
        print(images)
        exit(0)

    if args.image != None:
        image = args.image
        structures = Structures(structuresFolderPath, image)
        animation = structures.get(args.delay)
        animationJson = json.dumps(animation)
        print(animationJson)

        # structures.showAnimation(animation)

        exit(0)

    if args.text != None:
        text = args.text
        width, height = resolution
        fonts = Fonts(fontFullPath, height)
        letterImages = fonts.getText(text, resolution, args.colour)
        structures = Structures(letterImages)
        animation = structures.get(args.delay)
        animationJson = json.dumps(animation)
        print(animationJson)

        # structures.showAnimation(animation)

        exit(0)


if __name__ == "__main__":
    main()
