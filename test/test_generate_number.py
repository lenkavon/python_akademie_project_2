import unittest
from cows_and_bulls import generate_number


class TestGenerateNumber(unittest.TestCase):

    def test_generate_number_default(self):
        number = generate_number()
        self.assertEqual(len(str(number)), 4)

    def test_generate_number_figures_3(self):
        number = generate_number(figures=3)
        self.assertEqual(len(str(number)), 3)

    def test_generate_number_figures_7(self):
        number = generate_number(figures=7)
        self.assertEqual(len(str(number)), 7)

    def test_generate_number_invalid_figures_low(self):
        with self.assertRaises(ValueError):
            generate_number(figures=2)

    def test_generate_number_invalid_figures_high(self):
        with self.assertRaises(ValueError):
            generate_number(figures=8)

    def test_generate_number_repeat_digits(self):
        number = generate_number(figures=4, repeat_digits=True)
        self.assertEqual(len(str(number)), 4)

    def test_generate_number_no_repeat_digits(self):
        number = generate_number(figures=4, repeat_digits=False)
        self.assertEqual(len(set(str(number))), 4)


if __name__ == "__main__":
    unittest.main()
