from abc import abstractmethod

class Money:
    def __init__(self, amount, currency):
        self.__amount = amount
        self.__currency = currency
    
    def __eq__(self, object) -> bool:
        money = object
        return self.amount == money.amount and type(self) == type(money)
    # currencyメソッドを追加。インスタンス変数も追加
    def currency(self):
        return self.__currency

    @property
    def amount(self):
        return self.__amount
    # staticの戻り値に通貨を追加
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
    # 各コンストラクタとオーバーライドに引数currencyを設定
    
class Dollar(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)
        self.__amount = amount
        self.__currency = currency
    
    def times(self, multiplier: int):
        return Dollar(self.amount * multiplier)
    
    # -----------------
    
class Franc(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)
        self.__amount = amount
        self.__currency = currency
    
    def times(self, multiplier: int):
        return Franc(self.amount * multiplier)