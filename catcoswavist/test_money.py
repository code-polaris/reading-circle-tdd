import pytest
#testの構造: test_*で始まるを選択したため、test_*.pyで作成
from dollar import Dollar

class TestMoney:
    # class指定は()いらない、オブジェクト指定痔に()必要。
    # があると()インスタンスができる
    # ()がいらないクラス指定→staticメソッド
    def test_multiplication(self):
        
        five = Dollar(5)
        product = five.times(2)
        assert 10 == product.amount
        # この段階のproductはtostringを通していないのでただのアドレス(読めない)
        product = five.times(3)
        assert 15 == product.amount
        
TestMoney().test_multiplication()