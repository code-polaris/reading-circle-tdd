class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier: int):
        return Dollar(self.amount * multiplier)

