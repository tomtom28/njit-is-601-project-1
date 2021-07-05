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

    @classmethod
    def multiplication(cls, a, b):
        return int(a) * int(b)

    @classmethod
    def square(cls, a):
        return int(a) ** 2

    # Object Methods:
    def add(self, a, b):
        self.result = self.addition(a, b)
        return self.result

    def divide(self, a, b):
        self.result = self.division(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = self.multiplication(a, b)
        return self.result

    def squared(self, a):
        self.result = self.square(a)
        return self.result
