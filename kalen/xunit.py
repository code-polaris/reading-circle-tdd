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
        # 例外処理をさばく
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()

        self.tearDown()
        return result

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
        # エラーのデフォルト値を設定
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

# テストメソッドの中で例外をキャッチし出力できるようにする
print(TestCaseTest("testTemplateMethod").run().summary())
print(TestCaseTest("testResult").run().summary())
print(TestCaseTest("testfailedResult").run().summary())
print(TestCaseTest(" TestFailedResultFormatting").run().summary())