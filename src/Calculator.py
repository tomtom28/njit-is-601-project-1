import math


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
        return round(float(b) / float(a), 9)  # limit to 9 decimal places

    @classmethod
    def multiplication(cls, a, b):
        return int(a) * int(b)

    @classmethod
    def square(cls, a):
        return int(a) ** 2

    @classmethod
    def square_root(cls, a):
        c = math.sqrt(int(a))  # get result
        sigfig = math.floor(math.log(c, 10)) + 1  # number of significant digits in result
        return round(c, 9 - sigfig + 1)  # limit to 9 significant figures

    @classmethod
    def subtraction(cls, a, b):
        return int(b) - int(a)

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

    def sqrt(self, a):
        self.result = self.square_root(a)
        return self.result

    def subtract(self, a, b):
        self.result = self.subtraction(a, b)
        return self.result
