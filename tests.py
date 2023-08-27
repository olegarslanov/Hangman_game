"""
This file contains unit tests
"""

import unittest
from app import LifesCounter, HangmanPartsCounter


class TestLifesCounterClass(unittest.TestCase):
    """
    tests for correct lives calculate
    """

    def setUp(self):
        self.lifes_counter = LifesCounter()

    def test_get_result_method(self):
        self.assertEqual(10, self.lifes_counter.get_result())

    def test_reduce_lifes_method(self):
        self.lifes_counter.reduce_lifes()
        self.assertEqual(9, self.lifes_counter.get_result())


class TestHangmanPartsCounterClass(unittest.TestCase):
    """
    tests for correct Hangman parts calculate
    """

    def setUp(self):
        self.hangman_parts_counter = HangmanPartsCounter()

    def test_get_result_method(self):
        self.assertEqual(0, self.hangman_parts_counter.get_result())

    def test_reduce_lifes_method(self):
        self.hangman_parts_counter.count_parts()
        self.assertEqual(1, self.hangman_parts_counter.get_result())


# class TestWordGuessGameClass(unittest.TestCase):
#     """
#     tests for guess word correctly
#     """

#     def setUp(self):
#         self.hangman_part_counter = HangmanPartsCounter()
# //////
#     def test_get_result_method(self):
#         self.assertEqual(10, self.lifes_counter.get_result())

#     def test_reduce_lifes_method(self):
#         self.lifes_counter.reduce_lifes()
#         self.assertEqual(9, self.lifes_counter.get_result())


if __name__ == "__main__":
    unittest.main()
