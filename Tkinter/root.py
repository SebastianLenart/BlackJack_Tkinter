from tkinter import *
from PIL import ImageTk, Image
from deck import Deck
from word2number import w2n

global root
root = Tk()
root.title("BlackJack")
root.geometry("800x700")
root.configure(bg="green")

deck_test = Deck()
deck_test.insert_cards()


root.mainloop()
