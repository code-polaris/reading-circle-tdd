from dollar import Dollar
from franc import Franc
from money import Money

class TestMoney:
    def test_multiplication(self):
        # MoneyからDollarを返すように書き換える。Moneyクラスにstaticメソッドを設置する
        five = Money.dollar(5)
        assert five.times(2) == Money.dollar(10)
        assert five.times(3) == Money.dollar(15)

    def test_Equality(self):
        assert Money.dollar(5) == Money.dollar(5)
        assert not Money.dollar(5) == Money.dollar(6)
        assert Franc(5) == Franc(5)
        assert not Franc(5) == Franc(6)

    def test_FrancMultiplication(self):
        five = Franc(5)
        assert five.times(2) == Franc(10)
        assert five.times(3) == Franc(15)
        assert not Franc(5) == Money.dollar(5)



