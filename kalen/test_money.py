from money import Money
from money import Bank
from money import Sum

class TestMoney:
    def test_multiplication(self):
        five = Money.dollar(5)
        assert five * 2 == Money.dollar(10)
        assert five * 3 == Money.dollar(15)

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

    def test_ReduceSum(self):
        sum = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(sum, "USD")
        assert Money.dollar(7) == result

    def test_ReduceMoney(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), "USD")
        assert Money.dollar(1) == result

    def rest_ReducemoneyDifferentCurrency(self):
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        result = bank.reduce(Money.franc(2), "USD")
        assert Money.dollar(1) == result

    def test_MixedAddition(self):
        fiveBucks = Money.dollar(5)
        tenFrancs = Money.franc(10)
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        result = bank.reduce(fiveBucks + tenFrancs, "USD")
        assert Money.dollar(10) == result

    def test_SumPlusMoney(self):
        fiveBucks = Money.dollar(5)
        tenFrancs = Money.franc(10)
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        sum = Sum(fiveBucks, tenFrancs) + fiveBucks
        result = bank.reduce(sum, "USD")
        assert Money.dollar(15) == result

    def test_SumTimes(self):
        fiveBucks = Money.dollar(5)
        tenFrancs = Money.franc(10)
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        sum = Sum(fiveBucks, tenFrancs) * 2
        result = bank.reduce(sum, "USD")
        assert Money.dollar(20) == result

