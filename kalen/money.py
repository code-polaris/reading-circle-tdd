class Money:
    def __init__(self, amount):
        self.__amount = amount
    @property
    def amount(self):
        return self.__amount
    
    def __eq__(self, object) -> bool:
        money = object
        return self.amount == money.amount