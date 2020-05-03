#/usr/bin/env python3

import os
import argparse
import json
from pixels import Pixels
from structures import Structures
from fonts import Fonts

imagesFolder = "images/"
structuresFolder = "structures/"
fontPath = "fonts/code.ttf"
resolution = (8, 8)

def main():

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--update', default=False, type=bool, help='Regenerate structures from existing images')
    parser.add_argument('--speed', default=1000, type=int, help='Set animation speed')
    parser.add_argument('--colour', default=(255, 255, 255), type=object, help='Set font colour')
    parser.add_argument('--image', help='Get structures for image')
    parser.add_argument('--text', help='Get structures for text')
    parser.add_argument('--images', help='Get all available images')


    args = parser.parse_args()

    if args.update == True:
        # http://www.iconarchive.com/show/arcade-saturdays-icons-by-mad-science/Bashfull-Inky-icon.html
        # http://www.iconarchive.com/show/square-animal-icons-by-martin-berube.html
        for filename in os.listdir(imagesFolder):
            pixels = Pixels(imagesFolder, filename)
            pixels.save(resolution, structuresFolder)

    if args.images != None:
        images = []
        for filename in os.listdir(structuresFolder):
            file, ext = os.path.splitext(filename)
            name = file.split("_")[0]
            if name not in images:
                images.append(name)
        print(images)
        exit(0)

    if args.image != None:
        image = args.image
        structures = Structures(structuresFolder, image)
        animation = structures.get(args.speed)
        animationJson = json.dumps(animation)
        print(animationJson)
        exit(0)

    if args.text != None:
        text = args.text
        width, height = resolution
        fonts = Fonts(fontPath, height)
        letterImages = fonts.getText(text, resolution, args.colour)
        structures = Structures(letterImages)
        animation = structures.get(args.speed)
        animationJson = json.dumps(animation)
        print(animationJson)
        exit(0)


if __name__ == "__main__":
    main()
