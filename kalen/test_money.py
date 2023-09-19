from dollar import Dollar
from franc import Franc
from money import Money

class TestMoney:
    def test_multiplication(self):
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

    def test_Currency(self):
        assert Money.dollar(1).currency == "USD"
        assert Money.franc(1).currency == "CHF"
# 新しいテストを追加
    #def test_DifferentClassEquality(self):
        #assert Money(10, "CHF") == Franc(10, "CHF")


