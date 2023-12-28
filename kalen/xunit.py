# testMethodの動的な呼び出し
class WasRun:
    def __init__(self, name):
        self.wasRun = None
        # 文字列受け取り用変数
        self.name = name

    def run(self):
        # コンストラクタで受け取った文字列でメソッドを呼び出す
        method = getattr(self, self.name)
        # 実行　実際はtestMethodが動く
        method()

    def testMethod(self):
        self.wasRun = 1

test = WasRun("testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)