class TestCase:
    def __init__(self, name):
        self.name= name

    def setUp(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()

class WasRun(TestCase):    
    def setUp(self):
        self.wasRun = None
        self.log = "setUp "

    def testMethod(self):
        self.wasRun = 1
        # 追加で文字列がくっつくようにする
        self.log = self.log + "testMethod"

class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")

    def TestRunning(self):
        self.test.run()
        assert self.test.wasRun
    
    def TestSetUp(self):
        self.test.run()
        # テストする文字列内容を変更
        assert self.test.log == "setUp testMethod"
        
TestCaseTest("TestRunning").run()
TestCaseTest("TestSetUp").run()