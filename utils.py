import matplotlib.colors as colors

def rgb2hex(color):
    return colors.rgb2hex((color[0] / 255, color[1] / 255, color[2] / 255))[1:]

def hex2color(hex):
    color = colors.hex2color(hex)
    return (int(color[0] * 255), int(color[1] * 255), int(color[2] * 255))