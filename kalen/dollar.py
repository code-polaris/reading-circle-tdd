from money import Money
class Dollar(Money):
    def __init__(self, amount):
        super().__init__(amount)
        self.__amount = amount
    

    def times(self, multiplier: int):
        return Dollar(self.amount * multiplier)
    
    def __eq__(self, object: Money) -> bool:
        money = object
        return self.amount == money.amount

