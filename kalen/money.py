from abc import ABC, abstractmethod
class Expression(ABC):

    @abstractmethod
    def reduce(self, to: str):
        pass

    @abstractmethod
    def __add__(self, addend):
        pass
    # 抽象クラスにもtimesメソッドを設定
    @abstractmethod
    def __mul__(self, multiplier: int):
        pass

class Pair:
    def __init__(self, fromcurrency: str, to: str):
        self.fromcurrency = fromcurrency
        self.to = to
    def __eq__(self, something):
        pair = something
        return self.fromcurrency == pair.fromcurrency and self.to == pair.to
    
    def __hash__(self):
        return hash(0)

# ---------------------

class Bank:
    def __init__(self):
        self.rates = {}
    
    def reduce(self, source: Exception, to: str):
        if type(source) is Money:
            return source

        sum = source
        return sum.reduce(self, to)
    def addRate(self, fromcurrency: str, to: str, rate: int):
        curr_rate = Pair(fromcurrency, to)
        self.rates[curr_rate] = rate

    def rate(self, fromcurrency: str, to: str):
        curr_rate = Pair(fromcurrency, to)
        if fromcurrency == to:
            return 1
        return self.rates.get(curr_rate)

# ---------------------

class Sum(Expression):
    def __init__(self, augend, addend):
        self.__augend = augend
        self.__addend = addend
    @property
    def augend(self):
        return self.__augend
    @property
    def addend(self):
        return self.__addend
    
    def reduce(self, bank, to):
        amount = self.augend.reduce(bank, to).amount + self.addend.reduce(bank, to).amount
        return Money(amount, to)
    
    def __add__(self, addend):
        return Sum(self, addend)
    # timesメソッドを追加
    def __mul__(self, multiplier: int):
        return Sum(self.augend * multiplier, self.addend * multiplier)
    
# ---------------------

class Money(Expression):
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
        return self.__dict__ == object.__dict__

    def __add__(self, addend):
        return Sum(self, addend)

    def __mul__(self, multiplier: int):
        return Money(self.amount * multiplier, self.currency)
        
    def reduce(self, bank, to: str):
        rate = bank.rate(self.currency, to)
        return Money(self.amount / rate, to)
    