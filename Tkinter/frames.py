from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from deck import Deck
from word2number import w2n
from respond_button import Respond_button


class FrameButtons(Frame):
    OPTIONS = {"pady": 10}

    def __init__(self, container):
        super().__init__(container)
        self.parent = None
        self.configure(bg="white")
        self.columnconfigure(0, weight=1)
        self.pack(side=LEFT, fill=BOTH, expand=False)
        Label(self, text="\tFrameButtons\t").grid(row=0, column=0)
        self.hit_button = Button(self, text="HIT", state=DISABLED, command=self.hit)
        self.split_button = Button(self, text="SPLIT", state=DISABLED, command=self.split)
        self.stand_button = Button(self, text="STAND", state=DISABLED, command=self.stand)
        self.double_button = Button(self, text="DOUBLE", state=DISABLED, command=self.double)
        self.blackjack_button = Button(self, text="BLACKJACK", state=DISABLED, command=self.blackjack)
        self.insurance_button = Button(self, text="INSURANCE", state=DISABLED, command=self.insurance)
        self.exit_button = Button(self, text="EXIT", command=self.end_game)
        self.response = Respond_button()
        self.var = IntVar()
        self.update_grid()

    def upgrade_frame(self):
        self.configure(bg="white")
        self.columnconfigure(0, weight=1)
        self.pack(side=LEFT, fill=BOTH, expand=False)
        Label(self, text="\tFrameButtons\t").grid(row=0, column=0)

    def update_grid(self):
        self.hit_button.grid(self.OPTIONS, row=0, column=0, sticky=EW)
        self.split_button.grid(self.OPTIONS, row=1, column=0, sticky=EW)
        self.stand_button.grid(self.OPTIONS, row=2, column=0, sticky=EW)
        self.double_button.grid(self.OPTIONS, row=3, column=0, sticky=EW)
        self.blackjack_button.grid(self.OPTIONS, row=4, column=0, sticky=EW)
        self.insurance_button.grid(self.OPTIONS, row=5, column=0, sticky=EW)
        self.exit_button.grid(self.OPTIONS, row=6, column=0, sticky=EW)

    def set_parent(self, parent):
        self.parent = parent
    @staticmethod
    def end_game():
        exit()

    def hit(self):
        if not self.parent.insurance():
            self.parent.hit()
        self.parent.var.set(0)
        # self.hit_button.configure(state=DISABLED)

    def split(self):
        pass

    def stand(self):
        self.parent.var.set(2)
        self.parent.stand()

    def double(self):
        pass

    def blackjack(self):
        pass

    def insurance(self):
        self.parent.var.set(5)
        self.hit_button.configure(state=DISABLED)
        self.insurance_button.configure(state=DISABLED)



class FrameTable(Frame):
    def __init__(self, container):
        super().__init__(container)

        self.configure(bg="green")
        self.pack(side=LEFT, fill=BOTH, expand=True)

    def upgrade_frame(self):
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
        self.parent = None

        self.configure(bg="white")
        self.pack(side=LEFT, fill=BOTH, expand=False)
        Label(self, text="\tFrameResults\t").grid(row=0, column=0)
        self.selected_bet = StringVar()
        self.create_radio_buttons()
        # define variable
        self.all_money_label = Label(self, text=f"All money: {200110}")
        self.current_bet_label = Label(self, text=f"Current bet: {2000}")
        self.bet_label = Label(self, text="Choose value of bet:")
        self.button_confirm = Button(self, text="Confirm", command=self.set_value_bet)
        self.button_start = Button(self, text="START", bg="green", state=DISABLED, command=self.start)
        self.update_labels()

    def upgrade_frame(self):
        self.configure(bg="white")
        self.pack(side=LEFT, fill=BOTH, expand=False)

    def start(self):
        self.all_money_label.configure(text=f"All money: {self.parent.human.get_all_money()}")
        self.button_start.configure(state=DISABLED)
        self.parent.first_hand()

    def set_parent(self, parent):
        self.parent = parent

    def update_labels(self):
        self.all_money_label.grid(self.OPTIONS, row=1, column=0, sticky=EW)
        self.current_bet_label.grid(self.OPTIONS, row=2, column=0, sticky=EW)
        self.bet_label.grid(self.OPTIONS, row=3, column=0, sticky=EW)
        self.button_confirm.grid(self.OPTIONS, row=11, column=0, sticky=EW)
        self.button_start.grid(self.OPTIONS, row=12, column=0, sticky=EW, ipady=10)

    def set_value_bet(self):
        self.button_confirm.configure(state=DISABLED)
        self.current_bet_label = Label(self, text=f"Current bet: {self.selected_bet.get()}")
        self.update_labels()
        self.parent.make_bet(int(self.selected_bet.get()))
        self.button_start.configure(state=NORMAL)

    def get_value_radio_bet(self):
        return self.selected_bet.get()

    def create_radio_buttons(self):
        for e, bet in enumerate(self.BETS):
            bet_radio_button = ttk.Radiobutton(self, text=bet[0],
                                               value=bet[1],
                                               variable=self.selected_bet,
                                               )
            bet_radio_button.grid(row=4 + e, column=0, sticky=EW)
        self.selected_bet.set("50")
