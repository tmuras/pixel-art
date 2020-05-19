def rgb2hex(color):
    r = '{0:02x}'.format(color[0])
    g = '{0:02x}'.format(color[1])
    b = '{0:02x}'.format(color[2])
    return r + b + g

def hex2color(hex):
    r = hex[1:3]
    g = hex[3:5]
    b = hex[5:7]
    return (int(r, 16), int(g, 16), int(b, 16))