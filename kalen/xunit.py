class TestCase:
    def __init__(self, name):
        self.name= name

    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def run(self, result):
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()

        self.tearDown()
    
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
    

    def TestSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert self.result.summary() == "2 run, 1 failed"

suite = TestSuite()     
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testSuite"))

result = TestResult()
suite.run(result)
print(result.summary())
