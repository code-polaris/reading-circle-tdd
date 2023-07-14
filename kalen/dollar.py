from money import Money
class Dollar(Money):
    def __init__(self, amount):
        super().__init__(amount)
        self.__amount = amount
    

    def times(self, multiplier: int):
        return Dollar(self.amount * multiplier)

