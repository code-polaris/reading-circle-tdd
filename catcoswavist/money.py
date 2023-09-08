class Money:
    def __init__(self,amount):
        self._amount = amount
    @property
    def amount(self):
        return self._amount
        # 【疑問】kalen573さんの拝見 デコレータ@propertyをなぜ使うか疑問
        # 【疑問解決】アンダースコア(_)1個のほうがいい

    def equals(self,object) -> bool:
        if isinstance(object, Money):
            return self._amount == object.amount and type(self) == type(object)
        return
        # _amountのアンダースコア外す？外さない？
