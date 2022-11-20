from tkinter import *
from PIL import ImageTk, Image
# from root import root
# from tkinter import *


class Card:
    def __init__(self, figure, colour):
        self.figure = figure
        self.colour = colour
        self.value = None
        self.image = None

    def set_value(self, value: int):
        self.value = value

    def get_value(self):
        return self.value

    def get_figure(self):
        return self.figure

    def get_colour(self):
        return self.colour

    def set_image(self, path_image):
        self.image = path_image
        # print(self.figure, self.colour, self.image)
        # label_card = Label(root, image=self.image).pack()

    def __repr__(self):
        return f"{self.figure} : {self.colour}"

    def __str__(self):
        return f"{self.figure} : {self.colour}"
