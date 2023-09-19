#from abc import abstractmethod

class Money:
    def __init__(self, amount, currency):
        self.__amount = amount
        self.__currency = currency
    
    def __eq__(self, object) -> bool:
        #money = object
        return self.amount == object.amount and self.currency == object.currency

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
# アブストラクトメソッドから通常メソッドへ変更。Moneyクラスを返すようにする    
    #@abstractmethod
    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)
        #pass
    
    # -----------------
        
class Dollar(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)
# timesメソッドがMoneyクラスを返すようにする。Francも同じ
    def times(self, multiplier: int):
        return Money(self.amount * multiplier, self.currency)
    
    # -----------------
    
class Franc(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)
    
    def times(self, multiplier: int):
        return Money(self.amount * multiplier, self.currency)