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
    def __init__(self, name):
        self.wasRun = None
        super().__init__(name)
    
    def setUp(self):
        self.wasSetUp = 1

    def testMethod(self):
        self.wasRun = 1

class TestCaseTest(TestCase):
    def TestRunning(self):
        test = WasRun("testMethod")
        assert not test.wasRun
        test.run()
        assert test.wasRun
    # 新しいテストを追加
    def TestSetUp(self):
        test = WasRun("testMethod")
        test.run()
        assert test.wasSetUp
        
TestCaseTest("TestRunning").run()
TestCaseTest("TestSetUp").run()