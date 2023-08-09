from money import Money
# `class Dollar(Money):` ChatGPTで対応できず、理解していない。原因OPP・クラスの理解不足
# ↑ kanen573さんの拝見(https://github.com/code-polaris/reading-circle-tdd/commit/6643ed6dd5e11cd29f3a7b0923bb15c8de2bf6e7)
class Dollar(Money):
    def __init__(self,amount:int) -> int:
        # サブクラスから見えるように知るため、amount関数をprivateからprotectedに変更
        # Pythonにprotectedは存在しない → self.__amountのままでいい？
        self.__amount = amount
        # 【疑問】kalen573さんの拝見 デコレータ@propertyをなぜ使うか疑問
        # 【疑問】アンダースコア(_)1個？2個？
 
    @property
    def amount(self):
        return self.__amount

    def times(self, multiplier:int):
        return Dollar(self.__amount*multiplier)
    
    def equals(self,other):
        dollar = other
        return self.__amount == dollar.amount

