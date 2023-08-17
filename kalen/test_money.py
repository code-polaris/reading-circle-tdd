from dollar import Dollar
from franc import Franc

class TestMoney:
    def test_multiplication(self):
        five = Dollar(5)
        assert five.times(2) == Dollar(10)
        assert five.times(3) == Dollar(15)

    def test_Equality(self):
        assert Dollar(5) == Dollar(5)
        assert not Dollar(5) == Dollar(6)
        assert Franc(5) == Franc(5)
        assert not Franc(5) == Franc(6)

    def test_FrancMultiplication(self):
        five = Franc(5)
        assert five.times(2) == Franc(10)
        assert five.times(3) == Franc(15)
        # 新しいテストを追加
        assert not Franc(5) == Dollar(5)
        # この状態だとエラーになる、つまりフランとダラーは正しいことになっているが、それはおかしい。
        # 今は通貨概念をまだ導入していないので、Moneyクラスで実クラスが等しい時のみ等価比較を行うことにする



