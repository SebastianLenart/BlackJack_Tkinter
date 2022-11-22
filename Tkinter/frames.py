from tkinter import *
from PIL import ImageTk, Image
from deck import Deck
from word2number import w2n


class FrameButtons(Frame):
    def __init__(self, container):
        super().__init__(container)

        self.configure(bg="white")
        self.pack(side=LEFT, fill=BOTH, expand=False)
        Label(self, text="\tFrameButtons\t").pack(side=TOP)


class FrameTable(Frame):
    def __init__(self, container):
        super().__init__(container)

        self.configure(bg="green")
        self.pack(side=LEFT, fill=BOTH, expand=True)


class FrameResults(Frame):
    def __init__(self, container):
        super().__init__(container)

        self.configure(bg="white")
        self.pack(side=LEFT, fill=BOTH,  expand=False)
        Label(self, text="\tFrameResults\t").pack(side=TOP)
