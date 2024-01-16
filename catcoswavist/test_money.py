import pytest
#testの構造: test_*で始まるを選択したため、test_*.pyで作成
from dollar import Dollar
from franc import Franc
from money import Money

class TestMoney:
    # class指定は()いらない、オブジェクト指定時に()必要。
    # があると()インスタンスができる
    # ()がいらないクラス指定→staticメソッド
    def test_multiplication(self):
        
        # 【疑問】kalen573さんの拝見、この段階ではFrancはいじらない？
        #  MoneyからDollarを返すように書き換える。Moneyクラスにstaticメソッドを設置する
        five = Money.dollar(5)
        print(type(five),"\n",type(five.times(2)),"\n",type(Money.dollar(5)))
        assert five.times(2) == Money.dollar(10)
        # 原文MoneyTest.javaのassertEquals()はequalsを呼び出す
        # この段階のproductはdollars.py内でtostringを通していないのでただのアドレス(読めない)
        assert five.times(3) == Money.dollar(15)

        
    def test_equality(self):
        assert Dollar(5) == Money.dollar(5)
        assert not Dollar(5) == Money.dollar(6)
        assert Franc(5) == Franc(5)
        assert not Franc(5) == Franc(6)
        # ドルとフランが等価でないことを確認
        assert not Franc(5) == Money.dollar(5)

    def test_franc_multiplication(self):
        five = Franc(5)
        assert five.times(2) == Franc(10)
        assert five.times(3) == Franc(15)

if __name__ == '__main__':
    TestMoney().test_multiplication()
    TestMoney().test_franc_multiplication()
