import unittest
from src.handlers import operation_handlers

class TestHandlers(unittest.TestCase):    
    def test_sum_handler(self):
        num1 = 10
        num2 = 20
        expected_result = num1 + num2

        handler = operation_handlers.get(1)
        result = handler(num1, num2)

        self.assertEqual(result, f"The sum of {num1} and {num2} is {expected_result}.")

    def test_subtract_handler(self):
        num1 = 10
        num2 = 20
        expected_result = num1 - num2

        handler = operation_handlers.get(2)
        result = handler(num1, num2)

        self.assertEqual(result, f"The difference between {num1} and {num2} is {expected_result}.")

    def test_multiply_handler(self):
        num1 = 10
        num2 = 20
        expected_result = num1 * num2

        handler = operation_handlers.get(3)
        result = handler(num1, num2)

        self.assertEqual(result, f"The product of {num1} and {num2} is {expected_result}.")
