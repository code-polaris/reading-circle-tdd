from dollar import Dollar

class TestMoney:
    def test_multiplication(self):
        
        five = Dollar(5)
        five.times(2)
        assert 10 == five.amount

        five.times(3)
        assert 15 == five.amount

