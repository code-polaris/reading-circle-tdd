import pytest
#testの構造: test_*で始まるを選択したため、test_*.pyで作成
from dollar import Dollar

class TestMoney():
    def test_multiplication(self):
        
        five = Dollar(5)
        five.times(2)
        assert 10 == five.amount