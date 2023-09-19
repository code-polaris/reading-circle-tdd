from abc import ABC, abstractmethod
# 新しいクラスを追加
class Expression(ABC):
    pass

# ---------------------

class Bank:
    pass

# ---------------------

class Money:
    def __init__(self, amount, currency):
        self.__amount = amount
        self.__currency = currency
    
    @property
    def currency(self):
        return self.__currency

    @property
    def amount(self):
        return self.__amount
    
    @staticmethod
    def dollar(amount: int):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int):
        return Money(amount, "CHF")

    def __eq__(self, object) -> bool:
        return self.amount == object.amount and self.currency == object.currency

    def __add__(self, addend):
        return Money(self.__amount + addend.__amount, self.__currency)

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)