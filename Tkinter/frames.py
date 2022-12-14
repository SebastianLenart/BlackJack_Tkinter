from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from deck import Deck
from word2number import w2n


class FrameButtons(Frame):
    OPTIONS = {"pady": 10}
    split_mode = 0

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
        if self.split_mode == 0:
            if (self.parent.human.amount_of_cards == 0 and self.parent.insurance()) or self.parent.human.amount_of_cards == 0:
                self.parent.human.insert_cards(2)
                self.parent.human.display_cards()
                self.insurance_button.configure(state=DISABLED)
            else:
                self.parent.hit()
            self.parent.check_conditions_buttons()

            if self.parent.human.check_max_value() > self.parent.BLACK_JACK:
                self.parent.check_result(self.parent.human.get_best_value())
                messagebox.showinfo("Winner", self.parent.winner)
                self.parent.next_game()

        if self.split_mode == 2:
            self.hit_second_box_mode_split()
        if self.split_mode == 1:
            self.hit_first_box_mode_split()

    def hit_first_box_mode_split(self):
        self.parent.hit()
        if self.parent.human.check_max_value() > self.parent.BLACK_JACK:
            self.split_mode = 2

    def hit_second_box_mode_split(self):
        self.parent.hit_second_box()
        if self.parent.human.check_max_value_2_box() > self.parent.BLACK_JACK:
            self.check_results_in_split_mode()

    def split(self):
        self.split_mode = 1
        self.double_button.configure(state=DISABLED)
        self.split_button.configure(state=DISABLED)
        self.parent.split()

    def stand(self):
        if self.split_mode == 0:
            self.parent.stand()
            messagebox.showinfo("Winner", self.parent.winner)
            self.parent.next_game()
        if self.split_mode == 2:
            self.check_results_in_split_mode()
        if self.split_mode == 1:
            self.split_mode = 2

    def check_results_in_split_mode(self):
        self.parent.stand("Box 1")
        self.parent.croupier.display_cards()
        self.parent.check_result(self.parent.human.get_best_value_box2(), "Box 2", True)
        messagebox.showinfo("Winner", f"BOX 1: " + self.parent.winnerbox1 + "\n" +
                            f"BOX 2: " + self.parent.winnerbox2)
        self.parent.next_game()

    def double(self):
        self.double_button.configure(state=DISABLED)
        self.parent.double()
        messagebox.showinfo("Winner", self.parent.winner)
        self.parent.next_game()

    def blackjack(self):
        self.parent.blackjack()
        messagebox.showinfo("Winner", self.parent.winner)
        self.parent.next_game()

    def insurance(self):
        if self.parent.insurance() and self.parent.human.amount_of_cards == 0:
            self.parent.get_standard_award("5")
            self.parent.next_game()
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
        setattr(FrameButtons, "split_mode", 0)

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
