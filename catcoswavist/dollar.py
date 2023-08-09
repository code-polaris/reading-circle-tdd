from money import Money
class Dollar:
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

