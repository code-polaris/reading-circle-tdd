import pytest
#testの構造: test_*で始まるを選択したため、test_*.pyで作成
from dollar import Dollar
from franc import Franc

class TestMoney:
    # class指定は()いらない、オブジェクト指定痔に()必要。
    # があると()インスタンスができる
    # ()がいらないクラス指定→staticメソッド
    def test_multiplication(self):
        
        five = Dollar(5)
        assert five.times(2).equals(Dollar(10))
        # 原文MoneyTest.javaのassertEquals()はequalsを呼び出す
        print("product10:",Dollar(10),five.times(2))
        # この段階のproductはdollars.py内でtostringを通していないのでただのアドレス(読めない)
        assert five.times(3).equals(Dollar(15))
        print("product15:",Dollar(15),five.times(3))

        
    def test_equality(self):
        assert Dollar(5).equals(Dollar(5))
        assert not Dollar(5).equals(Dollar(6))

    def test_franc_multiplication(self):
        five = Franc(5)
        assert five.times(2).equals(Franc(10))
        print("franc10:",Franc(10),five.times(2))
        assert five.times(3).equals(Franc(15))
        print("franc15:",Franc(15),five.times(3))

if __name__ == '__main__':
    TestMoney().test_multiplication()
    TestMoney().test_franc_multiplication()
