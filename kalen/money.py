from abc import abstractmethod

class Money:
    def __init__(self, amount, currency):
        self.__amount = amount
        self.__currency = currency
    
    def __eq__(self, object) -> bool:
        money = object
        return self.amount == money.amount and self.currency == money.currency

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
    # timesメソッド共通化のために、一旦戻り値をサブクラスに戻す
    def times(self, multiplier: int):
    # 通貨を設定する
        return Dollar(self.amount * multiplier, "USD")
    
    # -----------------
    
class Franc(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)
    
    
    def times(self, multiplier: int):
        return Franc(self.amount * multiplier, "CHF")