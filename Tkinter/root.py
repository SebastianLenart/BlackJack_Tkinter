from tkinter import *
from PIL import ImageTk, Image
from deck import Deck
from word2number import w2n
from frames import FrameButtons, FrameTable, FrameResults


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Black Jack")
        self.geometry("1000x700")
        self.configure(bg="green")

        self.buttons = FrameButtons(self)
        self.table = FrameTable(self)
        self.results = FrameResults(self)

        self.deck = Deck(self.table)
        self.deck.insert_cards()


if __name__ == "__main__":
    app = App()
    app.mainloop()
