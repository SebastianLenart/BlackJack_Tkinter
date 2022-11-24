from tkinter import *
from PIL import ImageTk, Image
from deck import Deck
from word2number import w2n
from frames import FrameButtons, FrameTable, FrameResults
from game import Game


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Black Jack")
        self.geometry("1010x700")
        self.configure(bg="green")

        self.list_Frames = []
        self.buttons = FrameButtons(self)
        self.table = FrameTable(self)
        self.results = FrameResults(self)
        self.list_Frames.append(self.buttons)
        self.list_Frames.append(self.table)
        self.list_Frames.append(self.results)

        self.game = Game(self.list_Frames)


if __name__ == "__main__":
    app = App()
    app.mainloop()
