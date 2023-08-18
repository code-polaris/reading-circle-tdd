from dollar import Dollar
from franc import Franc
from money import Money

class TestMoney:
    def test_multiplication(self):
        # MoneyからFrancを返すように書き換える。Moneyクラスにstaticメソッドを設置する
        five = Money.dollar(5)
        assert five.times(2) == Money.dollar(10)
        assert five.times(3) == Money.dollar(15)

    def test_Equality(self):
        assert Money.dollar(5) == Money.dollar(5)
        assert not Money.dollar(5) == Money.dollar(6)
        assert Money.franc(5) == Money.franc(5)
        assert not Money.franc(5) == Money.franc(6)

    def test_FrancMultiplication(self):
        five = Money.franc(5)
        assert five.times(2) == Money.franc(10)
        assert five.times(3) == Money.franc(15)
        assert not Money.franc(5) == Money.dollar(5)



