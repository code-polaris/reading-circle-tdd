from abc import abstractmethod

class Money:
    def __init__(self, amount, currency):
        self.__amount = amount
        self.__currency = currency
    
    def __eq__(self, object) -> bool:
        money = object
        # type比較を通貨比較に変更する
        return self.amount == money.amount and self.currency == money.currency
    # currencyメソッドをproperty化する
    @property
    def currency(self):
        return self.__currency

    @property
    def amount(self):
        return self.__amount
    
    @staticmethod
    def dollar(amount: int):
        return Dollar(amount, "USD")
    
    @staticmethod
    def franc(amount: int):
        return Franc(amount, "CHF")
    
    @abstractmethod
    def times(self, multiplier):
        pass
    
    # -----------------
        
class Dollar(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)
    
    def times(self, multiplier: int):
        return Money.dollar(self.amount * multiplier)
    
    # -----------------
    
class Franc(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)
    
    
    def times(self, multiplier: int):
        return Money.franc(self.amount * multiplier)