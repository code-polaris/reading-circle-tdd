class TestCase:
    def __init__(self, name):
        self.name= name

    def setUp(self):
        pass
    # 空実装
    def tearDown(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        # 新たなメソッドを追加
        self.tearDown()

class WasRun(TestCase):    
    def setUp(self):
        self.log = "setUp "

    def testMethod(self):
        self.log = self.log + "testMethod "
    # 新たなログを追加
    def tearDown(self):
        self.log = self.log + "tearDown"

class TestCaseTest(TestCase):
    def TestTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert  test.log ==  "setUp testMethod tearDown"
        
TestCaseTest("TestTemplateMethod").run()