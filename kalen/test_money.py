from money import Money
from money import Bank

class TestMoney:
    def test_multiplication(self):
        five = Money.dollar(5)
        assert five.times(2) == Money.dollar(10)
        assert five.times(3) == Money.dollar(15)

    def test_Equality(self):
        assert Money.dollar(5) == Money.dollar(5)
        assert not Money.dollar(5) == Money.dollar(6)
        assert not Money.franc(5) == Money.dollar(5)
    
    def test_Currency(self):
        assert Money.dollar(1).currency == "USD"
        assert Money.franc(1).currency == "CHF"

    def test_SimpleAddition(self):
        five = Money.dollar(5)
        sum = five + five
        bank = Bank()
        reduce = bank.reduce(sum, "USD")
        assert Money.dollar(10) == reduce

    def test_PlusReturnsSum(self):
        five = Money.dollar(5)
        result = five + five
        sum = result
        assert five == sum.augend
        assert five == sum.addend

