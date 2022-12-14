from turtle import Turtle
import random

# rgb_colors = []
# colors = colorgram.extract("StarryNightFull4.jpg", 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
color_list = [(42, 106, 144), (16, 42, 61), (109, 165, 189), (23, 47, 42), (138, 176, 158), (76, 102, 90), (72, 147, 172), (51, 45, 37), (14, 65, 123), (177, 177, 121), (98, 95, 67), (206, 210, 136), (197, 223, 204), (222, 227, 188), (21, 79, 97), (182, 217, 232), (167, 207, 180), (182, 162, 42), (43, 75, 65), (98, 146, 134)]

class Color(Turtle)

    def __init__(self):
        super().__init__()
        self.color()

    def color_picker(self):
        self.color.random.ranint(color_list)


