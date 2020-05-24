#!/usr/bin/env python3

import sys
import os
import argparse
import json
from pixels import Pixels
from animation import Animation
from fonts import Fonts
from effects import Effects
from test import Test

# http://www.iconarchive.com
imagesFolder = "images/"
animationFolder = "animations/"
# http://sharefonts.net
fontPath = "fonts/5x7_practical.ttf"
resolution = (16, 64)


def main():

    path = os.path.dirname(sys.argv[0])

    imagesFolderPath = path + "/" + imagesFolder
    animationFolderPath  = path + "/" + animationFolder
    fontFullPath = path + "/" + fontPath

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--show', default=False, type=bool, help='Show animation')
    parser.add_argument('--update', default=False, type=bool, help='Re-create structures from existing images (default: False). True if images should be re-created')
    parser.add_argument('--delay', default=1000, type=int, help='Set delay in ms between animation frames - image, text, and effect (dafault: 1000)')
    parser.add_argument('--colour', default=[255, 255, 255], type=int, nargs=3, help='Set font colour in RGB format - 3 values between 0 and 255 (default: 255 255 255)')
    parser.add_argument('--parameters', default=[255, 255, 255], type=int, nargs='*', help='Set parameters for effect. For snakes use colour in RGB format. For rainbow use colour increment speed(integer) and number of frames')
    parser.add_argument('--font_size', default='large', help='Enter size of the font: small or large and effect: static or scroll')
    parser.add_argument('--font_effect', default='static', help='Enter effect for font: static or scroll')
    parser.add_argument('--image', help='Enter image name to get animation. Required option is delay')
    parser.add_argument('--text', help='Enter text to get animation. Required options are: colour, font and delay')
    parser.add_argument('--effect', help='Enter effect name to get animation. Required options are: parameters and delay')
    parser.add_argument('--images', help='Get list of all available image names to be used in image option')
    parser.add_argument('--effects', help='Get list of all available effect names to be used in effect option')
    parser.add_argument('--test', help='Get test matrix (only one frame)')
    # parser.print_help()

    args = parser.parse_args()
    args.colour = (args.colour[0], args.colour[1], args.colour[2])

    if args.update == True:
        # http://www.iconarchive.com/show/arcade-saturdays-icons-by-mad-science/Bashfull-Inky-icon.html
        # http://www.iconarchive.com/show/square-animal-icons-by-martin-berube.html
        for filename in os.listdir(imagesFolderPath):
            pixels = Pixels(imagesFolderPath, filename)
            pixels.save(resolution, animationFolderPath)

    if args.images != None:
        images = []
        for filename in os.listdir(animationFolderPath):
            file, ext = os.path.splitext(filename)
            name = file.split("_")[0]
            if name not in images:
                images.append(name)
        print(images)
        exit(0)

    if args.effects != None:
        effects = Effects()
        print(effects.list())
        exit(0)

    if args.image != None:
        animationObject = Animation(animationFolderPath, args.image)
        animation = animationObject.get(args.delay)
        animationJson = json.dumps(animation)
        print(animationJson)
        if args.show == True:
            animationObject.show(animation, resolution)
        exit(0)

    if args.text != None:
        fonts = Fonts(fontFullPath, args.font_size, args.font_effect, resolution)
        letterImages = fonts.getText(args.text, args.colour)
        animationObject = Animation(letterImages)
        animation = animationObject.get(args.delay)
        animationJson = json.dumps(animation)
        print(animationJson)
        if args.show == True:
            animationObject.show(animation, resolution)
        exit(0)

    if args.effect != None:
        effects = Effects(args.effect, resolution)
        pixelsArray = effects.get(args.parameters)
        animationObject = Animation(pixelsArray)
        animation = animationObject.get(args.delay)
        animationJson = json.dumps(animation)
        print(animationJson)
        if args.show == True:
            animationObject.show(animation, resolution)
        exit(0)

    if args.test != None:
        test = Test(resolution)
        pixelsArray = test.get()
        animationObject = Animation(pixelsArray)
        animation = animationObject.get(args.delay)
        animationJson = json.dumps(animation)
        print(animationJson)
        if args.show == True:
            animationObject.show(animation, resolution)
        exit(0)

if __name__ == "__main__":
    main()
