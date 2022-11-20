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
        # self.columnconfigure(0, weight=4)
        # self.columnconfigure(1, weight=1)
        # self.resizable(True, False) # limit X Y
        self.deck = Deck(self)
        # self.deck.configure(bg="green")
        # self.deck.grid(row=0, column=1)
        self.deck.insert_cards()

        # self.label = Label(self, text='Hello, Tkinter1!').pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()
