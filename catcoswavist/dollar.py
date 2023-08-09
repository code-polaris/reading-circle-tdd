from money import Money
# `class Dollar(Money):` ChatGPTで対応できず、理解していない。原因OPP・クラスの理解不足
# ↑ kanen573さんの拝見(https://github.com/code-polaris/reading-circle-tdd/commit/6643ed6dd5e11cd29f3a7b0923bb15c8de2bf6e7)
class Dollar(Money):
    def __init__(self,amount:int) -> int:
        # サブクラスで__init__を定義すると、親の__init__が上書きされてしまうためsuper()を使用？(参照:https://commte.net/7413)
        # これがないと`TypeError: Money.__init__() takes 1 positional argument but 2 were given`のエラー？
        super().__init__(amount)
        # サブクラスから見えるように知るため、amount関数をprivateからprotectedに変更
        # Pythonにprotectedは存在しない → self.__amountのままでいい？
        self.__amount = amount

    def times(self, multiplier:int):
        return Dollar(self.__amount*multiplier)
        # まだMoneyに変換しない、Dollarのまま(変更するとAttributeError: 'Money' object has no attribute 'equals'になった)
    
    def equals(self,object: Money) -> bool:
        money = object
        return self.__amount == money.amount

