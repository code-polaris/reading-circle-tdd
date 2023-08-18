from abc import abstractmethod

class Money:
    def __init__(self, amount):
        self.__amount = amount
    
    def __eq__(self, object) -> bool:
        money = object
        return self.amount == money.amount and type(self) == type(money)

    @property
    def amount(self):
        return self.__amount

    @staticmethod
    def dollar(amount: int):
        return Dollar(amount)
    # staticmethodでFrancを設置
    @staticmethod
    def franc(amount: int):
        return Franc(amount)
    
    @abstractmethod
    def times(self, multiplier):
        pass
    
    # -----------------
    
class Dollar(Money):
    def __init__(self, amount):
        super().__init__(amount)
        self.__amount = amount
    
    def times(self, multiplier: int):
        return Dollar(self.amount * multiplier)
    
    # -----------------
    
class Franc(Money):
    def __init__(self, amount):
        super().__init__(amount)
        self.__amount = amount
    
    # フランとダラーのタイムズメソッドを一致させMoneyに置けるようにする
    def times(self, multiplier: int):
        return Franc(self.amount * multiplier)