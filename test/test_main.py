import unittest
from context import cows_and_bulls
from unittest.mock import patch
from cows_and_bulls.main import cows_and_bulls

class TestCowsAndBulls(unittest.TestCase):

  @patch('builtins.input', side_effect=['y'])
  @patch('cows_and_bulls.main.generate_number')
  @patch('cows_and_bulls.main.guess_result')
  def test_basic_version(self, mock_guess_result, mock_generate_number, mock_input):
    mock_generate_number.return_value = '1234'
    cows_and_bulls()
    mock_generate_number.assert_called_once_with(figures=4, repeat_digits=False)
    mock_guess_result.assert_called_once_with('1234', 4, 10, False)

  @patch('builtins.input', side_effect=['n', '5', 'y'])
  @patch('cows_and_bulls.main.generate_number')
  @patch('cows_and_bulls.main.guess_result')
  def test_custom_version_with_repeats(self, mock_guess_result, mock_generate_number, mock_input):
    mock_generate_number.return_value = '12345'
    cows_and_bulls()
    mock_generate_number.assert_called_once_with(figures=5, repeat_digits=True)
    mock_guess_result.assert_called_once_with('12345', 5, 10, True)

  @patch('builtins.input', side_effect=['n', '6', 'n'])
  @patch('cows_and_bulls.main.generate_number')
  @patch('cows_and_bulls.main.guess_result')
  def test_custom_version_without_repeats(self, mock_guess_result, mock_generate_number, mock_input):
    mock_generate_number.return_value = '123456'
    cows_and_bulls()
    mock_generate_number.assert_called_once_with(figures=6, repeat_digits=False)
    mock_guess_result.assert_called_once_with('123456', 6, 10, False)

if __name__ == '__main__':
  unittest.main()