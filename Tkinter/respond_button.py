class Respond_button:
    def __init__(self):
        self.number = None
        self.name = None

    def set_parameters(self, number, name):
        self.number = number
        self.name = name

    def get_parameters(self):
        return [self.number, self.name]

    def set_default_parameters(self):
        self.number = None
        self.name = None
