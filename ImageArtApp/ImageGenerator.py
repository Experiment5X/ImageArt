import numpy as np
from math import sin, cos, tan


class ImageGenerator:
    def __init__(self, red_func, green_func, blue_func):
        self.red_func = red_func
        self.green_func = green_func
        self.blue_func = blue_func

    def get_image(self, width=500, height=500):
        image = np.zeros((width, height, 3))

        code = 'for y in range(0, height):\n'
        code += '\tfor x in range(0, width):\n'
        code += '\t\timage[y, x, 2] = ' + self.red_func + '\n'
        code += '\t\timage[y, x, 1] = ' + self.green_func + '\n'
        code += '\t\timage[y, x, 0] = ' + self.blue_func + '\n'
        exec(code)

        return image

