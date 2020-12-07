import unittest

from CreditCardValidation import *


class CreditCardValidationTest(unittest.TestCase):
    def setUp(self) -> None:
        print("setup... ")

    def test_validateCard_valid(self):
        result = ValidateCard(date(2021, 2, 3))
        self.assertEqual("Valid", result)

    def test_validateCard_expired(self):
        result = ValidateCard(date(2019, 12, 3))
        self.assertEqual("Expired", result)

    def tearDown(self) -> None:
        print("tearup....")


if __name__ == "__main__":
    unittest.main()
