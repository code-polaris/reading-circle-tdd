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
        assert product.equals(Dollar(10))
        # 原文MoneyTest.javaのassertEquals()はequalsを呼び出す
        print("product10:",Dollar(10),product)
        # この段階のproductはdollars.py内でtostringを通していないのでただのアドレス(読めない)
        product = five.times(3)
        assert product.equals(Dollar(15))
        print("product10:",Dollar(15),product)

        
    def test_equality(self):
        assert Dollar(5).equals(Dollar(5))
        assert not Dollar(5).equals(Dollar(6))

if __name__ == '__main__':
    TestMoney().test_multiplication()