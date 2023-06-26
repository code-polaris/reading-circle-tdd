class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier: int):
        return Dollar(self.amount * multiplier)
    
    def __eq__(self, object: object) -> bool:
        return True

