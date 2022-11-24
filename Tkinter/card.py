from tkinter import *
from PIL import ImageTk, Image
from tkinter import *
from PIL import ImageTk, Image


class Card:
    def __init__(self, figure, colour):
        self.figure = figure
        self.colour = colour
        self.value = None
        self.image_path = None
        self.my_img = None

    def set_value(self, value: int):
        self.value = value

    def get_value(self):
        return self.value

    def get_figure(self):
        return self.figure

    def get_colour(self):
        return self.colour

    def set_image_path(self, path_image):
        self.image_path = path_image

    def get_image_path(self):
        return self.image_path

    def set_image(self, path_image):
        image = Image.open(self.image_path)
        img = image.resize((int(image.width / 7), int(image.height / 7)))
        self.my_img = ImageTk.PhotoImage(img)

    def get_image(self):
        return self.my_img

    def __repr__(self):
        return f"{self.figure} : {self.colour}"

    def __str__(self):
        return f"{self.figure} : {self.colour}"
