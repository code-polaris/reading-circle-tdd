class TestCase:
    def __init__(self, name):
        self.name= name

    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    # runメソッドの変更
    def run(self, result):
        # result = TestResult()
        result.testStarted()
        self.setUp()
        # 例外処理をさばく
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()

        self.tearDown()
        #return result
    
class TestSuite:
    def __init__(self):
        self.tests = []
        
    def add(self, test):
        self.tests.append(test)
    
    def run(self, result): 
        for test in self.tests:
            test.run(result)

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
    # setUpの時にインスタンスを作る。
    #このsetUpメソッドはこのクラスが継承しているTestCaseクラスにあるsetUpメソッドをオーバーライドしている。
    def setUp(self):
        self.result = TestResult()

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        # result = TestResult()
        test.run(self.result)
        assert  test.log ==  "setUp testMethod tearDown"
    
    def testResult(self):
        test = WasRun("testMethod")
        # result = TestResult()
        test.run(self.result)
        assert self.result.summary() == "1 run, 0 failed"
    
    def testfailedResult(self):
        test = WasRun("testBrokenMethod")
        # result = TestResult()
        test.run(self.result)
        assert self.result.summary() == "1 run, 1 failed"

    def testFailedResultFormatting(self):
        # result = TestResult()
        self.result.testStarted()
        self.result.testFailed()
        assert self.result.summary() == "1 run, 1 failed"
    
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
        # result = TestResult()
        suite.run(self.result)
        assert self.result.summary() == "2 run, 1 failed"

# テストの実行部分を書き直す
suite = TestSuite()     
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testSuite"))

result = TestResult()
suite.run(result)
print(result.summary())
