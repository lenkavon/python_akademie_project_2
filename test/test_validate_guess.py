import unittest
from context import cows_and_bulls
from cows_and_bulls.validate_guess import validate_guess


class TestValidateGuess(unittest.TestCase):
    def test_valid_guess(self):
        self.assertTrue(validate_guess("1234", 4))

    def test_invalid_guess_with_repeated_digits(self):
        self.assertFalse(validate_guess("1123", 4))

    def test_invalid_guess_with_non_digit_characters(self):
        self.assertFalse(validate_guess("12a4", 4))

    def test_invalid_guess_with_incorrect_length(self):
        self.assertFalse(validate_guess("12345", 4))

    def test_valid_guess_with_repeated_digits_allowed(self):
        self.assertTrue(validate_guess("1123", 4, repeat_digits=True))

    def test_invalid_guess_with_incorrect_length_and_repeated_digits_allowed(self):
        self.assertFalse(validate_guess("12345", 4, repeat_digits=True))


if __name__ == "__main__":
    unittest.main()
