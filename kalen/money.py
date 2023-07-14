class Money:
    def __init__(self, amount):
        self.__amount = amount
    @property
    def amount(self):
        return self.__amount