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
        hit_button = Button(self, text="HIT", state=DISABLED)
        hit_button.grid(options, row=1, column=0, sticky=EW)

        hit_button = Button(self, text="STAND", state=DISABLED)
        hit_button.grid(options, row=2, column=0, sticky=EW)

        hit_button = Button(self, text="DOUBLE", state=DISABLED)
        hit_button.grid(options, row=3, column=0, sticky=EW)

        hit_button = Button(self, text="SPLIT", state=DISABLED)
        hit_button.grid(options, row=4, column=0, sticky=EW)

        hit_button = Button(self, text="BLACKJACK", state=DISABLED)
        hit_button.grid(options, row=5, column=0, sticky=EW)

        hit_button = Button(self, text="INSURANCE", state=DISABLED)
        hit_button.grid(options, row=6, column=0, sticky=EW)

        hit_button = Button(self, text="EXIT", state=DISABLED)
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

    OPTIONS = {"pady": 10}

    def __init__(self, container):
        super().__init__(container)

        self.configure(bg="white")
        self.pack(side=LEFT, fill=BOTH, expand=False)
        Label(self, text="\tFrameResults\t").grid(row=0, column=0)
        self.selected_bet = StringVar()
        self.create_radio_buttons()
        # define variable
        self.all_money_label = Label(self, text=f"All money: {200110}")
        self.current_bet_label = Label(self, text=f"Current bet: {2000}")
        self.bet_label = Label(self, text="Choose value of bet:")
        self.button_confirm = Button(self, text="Confirm")
        self.button_start = Button(self, text="START", bg="green", state=DISABLED)
        self.update_labels()

    def update_labels(self):
        self.all_money_label.grid(self.OPTIONS, row=1, column=0, sticky=EW)
        self.current_bet_label.grid(self.OPTIONS, row=2, column=0, sticky=EW)
        self.bet_label.grid(self.OPTIONS, row=3, column=0, sticky=EW)
        self.button_confirm.grid(self.OPTIONS, row=11, column=0, sticky=EW)
        self.button_start.grid(self.OPTIONS, row=12, column=0, sticky=EW, ipady=10)

    def create_radio_buttons(self):
        for e, bet in enumerate(self.BETS):
            bet_radio_button = ttk.Radiobutton(self, text=bet[0],
                                               value=bet[1],
                                               variable=self.selected_bet,
                                               )
            bet_radio_button.grid(row=4 + e, column=0, sticky=EW)
