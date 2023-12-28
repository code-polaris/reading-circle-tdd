class TestCase:
    def __init__(self, name):
        self.name= name
    # setupメソッドを設定
    def setUp(self):
        pass

    def run(self):
        # setUpを呼ぶ責務はTestCaseにこそあるべき
        self.setUp()
        method = getattr(self, self.name)
        method()

class WasRun(TestCase):    
    def setUp(self):
        # wasRunフラグを移動　コンストラクタは削除
        # これでsetUp起動のたびにwasRunが初期化される
        self.wasRun = None
        self.wasSetUp = 1

    def testMethod(self):
        self.wasRun = 1
# テストをシンプルに書き直す
class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")
        
    def TestRunning(self):
        self.test.run()
        assert self.test.wasRun
    
    def TestSetUp(self):
        self.test.run()
        assert self.test.wasSetUp
        
TestCaseTest("TestRunning").run()
TestCaseTest("TestSetUp").run()