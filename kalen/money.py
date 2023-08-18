class Money:
    def __init__(self, amount):
        self.__amount = amount
    @property
    def amount(self):
        return self.__amount
    
    def __eq__(self, object) -> bool:
        money = object
        return self.amount == money.amount and type(self) == type(money)

    # 静的メソッドを追加。この時クラスのインポートがループするためMoneyクラスファイルにサブクラスも置くようにする
    # classmethodにしない理由は、dollarメソッドが特にクラスのバックグラウンドを必要としないため。
    @staticmethod
    def dollar(amount: int):
        return Dollar(amount)
    
    # -----------------
    
class Dollar(Money):
    def __init__(self, amount):
        super().__init__(amount)
        self.__amount = amount
    
    # フランとダラーのタイムズメソッドを一致させMoneyに置けるようにする
    def times(self, multiplier: int):
        return Dollar(self.amount * multiplier)