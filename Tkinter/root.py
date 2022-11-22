from tkinter import *
from PIL import ImageTk, Image
from deck import Deck
from word2number import w2n


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Black Jack")
        self.geometry("800x700")
        self.configure(bg="green")

        # self.deck = Deck(self)
        # self.deck.insert_cards()

        self.buttonsFrame = Frame(self, bg="blue")
        self.buttonsFrame.pack(side=LEFT, fill=BOTH, expand=True)
        self.label = Label(self.buttonsFrame, text="fdadf").pack()

        self.RFrame = Frame(self, bg="red")
        self.RFrame.pack(side=LEFT, fill=BOTH, expand=True)
        self.label = Label(self.RFrame, text="sss").pack(side=TOP)


if __name__ == "__main__":
    app = App()
    app.mainloop()
