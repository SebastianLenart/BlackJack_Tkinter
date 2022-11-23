from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from deck import Deck
from word2number import w2n


class FrameButtons(Frame):
    def __init__(self, container):
        super().__init__(container)

        self.configure(bg="white")
        self.columnconfigure(0, weight=1)
        self.pack(side=LEFT, fill=BOTH, expand=False)
        Label(self, text="\tFrameButtons\t").grid(row=0, column=0)
        self.create_buttons()

    def create_buttons(self):
        options = {'pady': 10}
        hit_button = Button(self, text="HIT")
        hit_button.grid(options, row=1, column=0, sticky=EW)

        hit_button = Button(self, text="STAND")
        hit_button.grid(options, row=2, column=0, sticky=EW)

        hit_button = Button(self, text="DOUBLE")
        hit_button.grid(options, row=3, column=0, sticky=EW)

        hit_button = Button(self, text="SPLIT")
        hit_button.grid(options, row=4, column=0, sticky=EW)

        hit_button = Button(self, text="BLACKJACK", state=DISABLED)
        hit_button.grid(options, row=5, column=0, sticky=EW)

        hit_button = Button(self, text="INSURANCE")
        hit_button.grid(options, row=6, column=0, sticky=EW)

        hit_button = Button(self, text="EXIT")
        hit_button.grid(options, row=7, column=0, sticky=EW)


class FrameTable(Frame):
    def __init__(self, container):
        super().__init__(container)

        self.configure(bg="green")
        self.pack(side=LEFT, fill=BOTH, expand=True)


class FrameResults(Frame):
    BETS = (("50", 50),
            ("100", 100),
            ("500", 500,),
            ("1000", 1000),
            ("1500", 1500),
            ("2000", 2000),
            ("2002", 2002))

    def __init__(self, container):
        super().__init__(container)

        self.configure(bg="white")
        self.pack(side=LEFT, fill=BOTH, expand=False)
        Label(self, text="\tFrameResults\t").grid(row=0, column=0)
        self.selected_bet = StringVar()
        self.bets()

    def bets(self):
        options = {'pady': 10}
        all_money_label = Label(self, text=f"All money: {2000}")
        all_money_label.grid(options, row=1, column=0, sticky=EW)

        current_bet_label = Label(self, text=f"Current bet: {2000}")
        current_bet_label.grid(options, row=2, column=0, sticky=EW)

        bet_label = Label(self, text="Choose value of bet:")
        bet_label.grid(options, row=3, column=0, sticky=EW)

        for e, bet in enumerate(self.BETS):
            bet_radio_button = ttk.Radiobutton(self, text=bet[0],
                                               value=bet[1],
                                               variable=self.selected_bet,
                                               )
            bet_radio_button.grid(row=4 + e, column=0, sticky=EW)

        button_confirm = Button(self, text="Confirm")
        button_confirm.grid(options, row=11, column=0, sticky=EW)
