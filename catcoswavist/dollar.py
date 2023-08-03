class Dollar:
    def __init__(self,amount:int) -> int:
        self.amount = amount

    def times(self, multiplier:int):
        return Dollar(self.amount*multiplier)
    def equals(self,other):
        dollar = other
        return self.amount == dollar.amount

