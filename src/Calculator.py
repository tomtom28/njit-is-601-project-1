class Calculator:

    # Class Methods:
    @classmethod
    def addition(cls, a, b):
        return int(a) + int(b)

    # Initialization:
    result = 0

    def __init__(self):
        pass

    # Object Methods:
    def add(self, a, b):
        self.result = self.addition(a, b)
        return self.result
