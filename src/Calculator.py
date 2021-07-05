class Calculator:

    # Initialization:
    result = 0

    def __init__(self):
        pass

    # Class Methods:
    @classmethod
    def addition(cls, a, b):
        return int(a) + int(b)

    @classmethod
    def division(cls, a, b):
        return round(float(b) / float(a), 9)  # limit to 9 significant digits

    # Object Methods:
    def add(self, a, b):
        self.result = self.addition(a, b)
        return self.result

    def divide(self, a, b):
        self.result = self.division(a, b)
        return self.result
