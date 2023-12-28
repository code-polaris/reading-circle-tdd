class TestCase:
    def __init__(self, name):
        self.name= name

    def setUp(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
# 不必要になったフラグを削除
class WasRun(TestCase):    
    def setUp(self):
        self.log = "setUp "

    def testMethod(self):
        self.log = self.log + "testMethod"

class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")
    # テスト変更
    def TestTemplateMethod(self):
        self.test.run()
        assert  self.test.log ==  "setUp testMethod"
        
TestCaseTest("TestTemplateMethod").run()