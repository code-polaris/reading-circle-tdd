class TestCase:
    def __init__(self, name):
        self.name= name
        
# TestCaseクラスを継承
class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        # スーパー関数でnameを引き継ぐ
        super().__init__(name)

    def run(self):
        method = getattr(self, self.name)
        method()

    def testMethod(self):
        self.wasRun = 1

test = WasRun("testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)