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
        self.wasSetUp = 1
        # 記録用のログを保持できるようにする
        self.log = "setUp"

    def testMethod(self):
        self.wasRun = 1

class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")

    def TestRunning(self):
        self.test.run()
        assert self.test.wasRun
    
    def TestSetUp(self):
        self.test.run()
        # ログを見るテストに変更
        assert "setUp" == self.test.log
        
TestCaseTest("TestRunning").run()
TestCaseTest("TestSetUp").run()