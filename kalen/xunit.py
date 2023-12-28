class TestCase:
    def __init__(self, name):
        self.name= name

    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    # runメソッドの変更
    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return result

class WasRun(TestCase):    
    def setUp(self):
        self.log = "setUp "

    def testMethod(self):
        self.log = self.log + "testMethod "
    # 例外を発生させる
    def testBrokenMethod(self):
        raise Exception
    
    def tearDown(self):
        self.log = self.log + "tearDown"

class TestResult:

    def __init__(self):
        self.runCount = 0
    
    def testStarted(self):
        self.runCount += 1

    def summary(self):
        return "{0} run, 0 failed" .format(self.runCount)

class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert  test.log ==  "setUp testMethod tearDown"
    
    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert result.summary() == "1 run, 0 failed"

    # ちゃんと動かせるまで一旦コメントアウトする
    # def testfailedResult(self):
    #     test = WasRun("testBrokenMethod")
    #     result = test.run()
    #     assert result.summary() == "1 run, 1 failed"
        
TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
TestCaseTest("testfailedResult").run