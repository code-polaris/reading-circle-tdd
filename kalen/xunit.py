class TestCase:
    def __init__(self, name):
        self.name= name

    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    # runメソッドの変更
    def run(self, result):
        result = TestResult()
        result.testStarted()
        self.setUp()
        # 例外処理をさばく
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()

        self.tearDown()
        return result
    
class TestSuite:
    def __init__(self):
        self.tests = []
        
    def add(self, test):
        self.tests.append(test)
    
    def run(self, result): # 引数を追加
        # #インスタンスはテストの方で作る
        #result = TestResult()
        for test in self.tests:
            test.run(result)
        # ここに戻り値を明示せずともテストの方で返せる
        # return result

class WasRun(TestCase):    
    def setUp(self):
        self.log = "setUp "

    def testMethod(self):
        self.log = self.log + "testMethod "
    
    def testBrokenMethod(self):
        raise Exception
    
    def tearDown(self):
        self.log = self.log + "tearDown"

class TestResult:

    def __init__(self):
        self.runCount = 0
        self.errorCount = 0
    
    def testStarted(self):
        self.runCount += 1
    def testFailed(self):
        self.errorCount += 1
    def summary(self):
        return "{0} run, {1} failed" .format(self.runCount, self.errorCount)

class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert  test.log ==  "setUp testMethod tearDown"
    
    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert result.summary() == "1 run, 0 failed"
    
    def testfailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert result.summary() == "1 run, 1 failed"

    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert result.summary() == "1 run, 1 failed"
    
    """
    呼び出し側、つまりテストコードの方でTestResultインスタンスを作れば、TestSuiteのrunでは
    深い構造を持たなくともforを回せる。これはCollectingParameterPatternと呼ばれる。
    これは少し難しい構造デザイン(´・ω・｀)
    """
    def TestSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        # TestSuiteの中ではなく、テスト側でTestResultインスタンスを作る
        result = TestResult()
        result = suite.run(result)
        assert result.summary() == "2 run, 1 failed"

print(TestCaseTest("testTemplateMethod").run().summary())
print(TestCaseTest("testResult").run().summary())
print(TestCaseTest("testfailedResult").run().summary())
print(TestCaseTest(" TestFailedResultFormatting").run().summary())
print(TestCaseTest("TestSuite").run().summary())