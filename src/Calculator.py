import math


# Static Methods:
def addition(a, b):
    return int(a) + int(b)


def division(a, b):
    return round(float(b) / float(a), 9)  # limit to 9 decimal places


def multiplication(a, b):
    return int(a) * int(b)


def square(a):
    return int(a) ** 2


def square_root(a):
    c = math.sqrt(int(a))  # get result
    sigfig = math.floor(math.log(c, 10)) + 1  # number of significant digits in result
    return round(c, 9 - sigfig + 1)  # limit to 9 significant figures


def subtraction(a, b):
    return int(b) - int(a)


class Calculator:
    # Initialization:
    result = 0

    def __init__(self):
        pass

    # Object Methods:
    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def sqrt(self, a):
        self.result = square_root(a)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result
