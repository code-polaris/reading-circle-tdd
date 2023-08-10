from money import Money
class Franc(Money):
    def __init__(self,amount:int) -> int:
        # サブクラスで__init__を定義すると、親の__init__が上書きされてしまうためsuper()を使用？(参照:https://commte.net/7413)
        # これがないと`TypeError: Money.__init__() takes 1 positional argument but 2 were given`のエラー？
        super().__init__(amount)
        # サブクラスから見えるように知るため、amount関数をprivateからprotectedに変更
        # Pythonにprotectedは存在しない → self.__amountのままでいい？
        self.__amount = amount
 
    def times(self, multiplier:int):
        return Franc(self.__amount*multiplier)
    
    # equalメソッドでのFrancクラス→Moneyクラス、段階的にできず一気にやっちゃった