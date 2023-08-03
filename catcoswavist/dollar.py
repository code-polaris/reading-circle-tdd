class Dollar:
    def __init__(self,amount:int) -> int:
        self.amount = amount

    def times(self, multiplier:int):
        print("amount",self.amount)
        return Dollar(self.amount*multiplier)
    # どうやったらテスト通るか？第2章読み直し
    # なぜintじゃなくてDollarにしたか？
    
    # ->前のコードでは、最初のtimes呼び出しで5ドルが10ドルになる(再帰)
    # -> timesの呼び出し時には掛け算をせず、
    # returnするときだけ掛け算をすることで再帰回避
    # 【疑問】テストは通ったが、出力が見えない。
    # python .\test_money.py > output.txtしたのに白紙。
