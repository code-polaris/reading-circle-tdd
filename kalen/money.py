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
        return Money(amount, "USD")
    # サブクラスを削除する準備としてMoneyクラスを返すようにする
    @staticmethod
    def franc(amount: int):
        return Money(amount, "CHF")

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)
        #pass
    
    # -----------------
# Dollarクラスを参照しているテストはないのでDollarクラスは削除する        
# class Dollar(Money):
#     def __init__(self, amount, currency):
#         super().__init__(amount, currency)
   
    # -----------------
    
class Franc(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)