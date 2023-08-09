class Money:
    def __init__(self,amount):
        self.__amount = amount
    @property
    def amount(self):
        return self.__amount
        # 【疑問】kalen573さんの拝見 デコレータ@propertyをなぜ使うか疑問
        # 【疑問】アンダースコア(_)1個？2個？
