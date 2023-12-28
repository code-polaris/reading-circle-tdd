class TestCase:
    def __init__(self, name):
        self.name= name

    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return TestResult()

class WasRun(TestCase):    
    def setUp(self):
        self.log = "setUp "

    def testMethod(self):
        self.log = self.log + "testMethod "
    
    def tearDown(self):
        self.log = self.log + "tearDown"

class TestResult:
    def summary(self):
        return "1 run, 0 failed"

class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert  test.log ==  "setUp testMethod tearDown"
    # 新たなテストを追加
    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert result.summary() == "1 run, 0 failed"
        
TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()