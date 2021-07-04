import unittest
import TestProperties

from Calculator import Calculator
from CsvReader import CsvReader



class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_calculator_instantiate(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_calculator_addition(self):
        test_data = CsvReader(TestProperties.ADDITION_FILE_NAME).data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))


if __name__ == '__main__':
    unittest.main()
