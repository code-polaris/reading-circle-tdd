class Money:
    def __init__(self,amount):
        self.__amount = amount
    @property
    def amount(self):
        return self.__amount
        # 【疑問】kalen573さんの拝見 デコレータ@propertyをなぜ使うか疑問
        # 【疑問】アンダースコア(_)1個？2個？

    def equals(self,object) -> bool:
        money = object
        return self.__amount == money.amount
        # __amountのアンダースコア外す？外さない？
