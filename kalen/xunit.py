class TestCase:
    def __init__(self, name):
        self.name= name
    # runメソッドを引き上げ
    def run(self):
        method = getattr(self, self.name)
        method()

class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        super().__init__(name)

    def testMethod(self):
        self.wasRun = 1

test = WasRun("testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)