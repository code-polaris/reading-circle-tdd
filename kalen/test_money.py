from dollar import Dollar

class TestMoney:
    def test_multiplication(self):
        five = Dollar(5)
        assert five.times(2) == Dollar(10)
        assert five.times(3) == Dollar(15)

    def test_Equality(self):
        assert Dollar(5) == Dollar(5)
        assert not Dollar(5) == Dollar(6)

    def test_FrancMultiplication(self):
        five = Franc(5)
        assert five.times(2) == Franc(10)
        assert five.times(3) == Franc(15)


