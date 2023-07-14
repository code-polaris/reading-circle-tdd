from money import Money
class Dollar(Money):
    def __init__(self, amount):
        self.__amount = amount
    @property
    def amount(self):
        return self.__amount

    def times(self, multiplier: int):
        return Dollar(self.amount * multiplier)
    
    def __eq__(self, object: object) -> bool:
        dollar = object
        return self.amount == dollar.amount

