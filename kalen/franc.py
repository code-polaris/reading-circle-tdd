class Franc:
    def __init__(self, amount):
        self.__amount = amount
    @property
    def amount(self):
        return self.__amount

    def times(self, multiplier: int):
        return Franc(self.amount * multiplier)
    
    def __eq__(self, object: object) -> bool:
        franc = object
        return self.amount == franc.amount