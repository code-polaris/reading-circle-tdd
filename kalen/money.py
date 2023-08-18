class Money:
    def __init__(self, amount):
        self.__amount = amount
    @property
    def amount(self):
        return self.__amount
    
    def __eq__(self, object) -> bool:
        money = object
        return self.amount == money.amount and type(self) == type(money)
    # and type(self) == type(money) この部分がテストでフランとダラーを比べるとき、
    # 同じ通貨同士の時のみ等価比較させるようにする部分
    # これでテストは通ります。
    # これが第7章の変更部分