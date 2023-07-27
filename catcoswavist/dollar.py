class Dollar:
    def __init__(self,amount:int) -> int:
        self.amount = amount

    def times(self, multiplier:int) -> int:
        self.amount *= multiplier
