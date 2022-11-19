class Card:
    def __init__(self, figure, colour):
        self.figure = figure
        self.colour = colour
        self.value = None

    def set_value(self, value: int):
        self.value = value

    def get_value(self):
        return self.value

    def get_figure(self):
        return self.figure

    def __repr__(self):
        return f"{self.figure} : {self.colour}"

    def __str__(self):
        return f"{self.figure} : {self.colour}"