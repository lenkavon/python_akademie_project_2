import unittest
from context import cows_and_bulls
from unittest.mock import patch
from cows_and_bulls.guess_result import guess_result

class TestGuessResult(unittest.TestCase):

  @patch('builtins.input', side_effect=['1234'])
  @patch('builtins.print')
  def test_correct_guess(self, mock_print, mock_input):
    guess_result(1234, 4, 10, False)
    mock_print.assert_any_call("Gratulujeme, uhodli jste cislo!")

  @patch('builtins.input', side_effect=['5678', '1234'])
  @patch('builtins.print')
  def test_incorrect_then_correct_guess(self, mock_print, mock_input):
    guess_result(1234, 4, 10, False)
    mock_print.assert_any_call("Tip: 5678 -> Cows: 0 Bulls: 0, Zbyva pokusu: 9")
    mock_print.assert_any_call("Gratulujeme, uhodli jste cislo!")

  @patch('builtins.input', side_effect=['5678', '4321', '1234'])
  @patch('builtins.print')
  def test_multiple_incorrect_then_correct_guess(self, mock_print, mock_input):
    guess_result(1234, 4, 10, False)
    mock_print.assert_any_call("Tip: 5678 -> Cows: 0 Bulls: 0, Zbyva pokusu: 9")
    mock_print.assert_any_call("Tip: 4321 -> Cows: 4 Bulls: 0, Zbyva pokusu: 8")
    mock_print.assert_any_call("Gratulujeme, uhodli jste cislo!")

  @patch('builtins.input', side_effect=['5678', '4321'])
  @patch('builtins.print')
  def test_out_of_attempts(self, mock_print, mock_input):
    guess_result(1234, 4, 2, False)
    mock_print.assert_any_call("Tip: 5678 -> Cows: 0 Bulls: 0, Zbyva pokusu: 1")
    mock_print.assert_any_call("Tip: 4321 -> Cows: 4 Bulls: 0, Zbyva pokusu: 0")
    mock_print.assert_any_call("Bohuzel jste neuhodli cislo.")
    mock_print.assert_any_call("Spravne cislo bylo: 1234")

if __name__ == '__main__':
  unittest.main()